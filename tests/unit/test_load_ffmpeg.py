#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import pytest
import os
import pyglet_ffmpeg


def test_ffmpeg_unavailable():
    from pyglet.media import have_ffmpeg
    assert not have_ffmpeg()


def test_binaries_not_found(mocker, capsys):
    mocker.patch("pyglet_ffmpeg.loader._locate_binaries")
    pyglet_ffmpeg.load_ffmpeg()
    out, err = capsys.readouterr()
    assert out == "FFmpeg binaries could not be loaded.\n"


@pytest.mark.parametrize("platform, arch, expected", [
    ("win32", 2 ** 32, "Win32"),
    ("win32", 2 ** 64, "Win64"),
    ("darwin", 2 ** 64, "MacOS"),
    ("linux", 2 ** 64, "linux_x86_64"),
    ("linux-armv7l", 2 ** 32, "RPi"),
])
def test_locate_binaries(platform, arch, expected, mocker):
    mocker.patch("sys.platform", platform)
    mocker.patch("sys.maxsize", arch)
    mocksym = mocker.patch("pyglet_ffmpeg.loader._ensure_linux_symlinks")
    mockloader = mocker.patch("pyglet.lib.loader")

    pyglet_ffmpeg.loader._locate_binaries()

    env_var = "PATH" if platform == "win32" else "LD_LIBRARY_PATH"
    expected_path = os.path.join("pyglet-ffmpeg", "pyglet_ffmpeg", expected)
    assert expected_path in os.environ[env_var]

    if platform.startswith("linux"):
        mockloader._create_ld_so_cache.assert_called_once()
        mocksym.assert_called_once()


def test_load_ffmpeg():
    import pyglet
    pyglet_ffmpeg.load_ffmpeg()
    assert pyglet.media.have_ffmpeg()


def test_ensure_linux_symlinks(mocker):
    def glob_side_effet(filename):
        "Returns a fake so filename based on the argument"
        return [filename[:-1] + "1.2"]

    mocker.patch("glob.glob", side_effect=glob_side_effet)
    mocker.patch("os.path.isfile", return_value=False)
    mocksym = mocker.patch("os.symlink")

    bin_folder = os.path.normpath("path/to/lib")
    pyglet_ffmpeg.loader._ensure_linux_symlinks(bin_folder)

    sofiles = (
        "libavcodec.so.58.1.2", "libavformat.so.58.1.2", "libswresample.so.3.1.2",
        "libavfilter.so.7.1.2", "libavutil.so.56.1.2", "libswscale.so.5.1.2"
    )
    expected = list()
    for sofile in sofiles:
        parts = sofile.split(".")
        for length in (3, 2):
            link = ".".join(parts[:length])
            call = mocker.call(
                os.path.join(bin_folder, sofile),
                os.path.join(bin_folder, link)
            )
            expected.append(call)

    assert mocksym.call_args_list == expected
