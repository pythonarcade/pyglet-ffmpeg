#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import pytest
import os
import pyglet_ffmpeg


def test_ffmpeg_unavailable():
    from pyglet.media import have_ffmpeg
    assert not have_ffmpeg()


@pytest.mark.parametrize('platform, arch, expected', [
    ('win32', 2 ** 32, 'Win32'),
    ('win32', 2 ** 64, 'Win64'),
    ('darwin', 2 ** 64, 'MacOS'),
])
def test_locate_binaries(platform, arch, expected, mocker):
    mocker.patch('sys.platform', platform)
    mocker.patch('sys.maxsize', arch)

    pyglet_ffmpeg.loader._locate_binaries()

    env_var = 'PATH' if platform == 'win32' else 'LD_LIBRARY_PATH'
    expected_path = os.path.join('pyglet-ffmpeg', 'pyglet_ffmpeg', expected)
    assert expected_path in os.environ[env_var]


def test_load_ffmpeg():
    import pyglet
    pyglet_ffmpeg.load_ffmpeg()
    assert pyglet.media.have_ffmpeg()
