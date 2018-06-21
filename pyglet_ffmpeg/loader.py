#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""This module provides functions for loading FFmpeg binaries.
"""

import sys
import os
import pyglet.media


def load_ffmpeg():
    """Load FFmpeg binaries.
    """

    _locate_binaries()
    if pyglet.media.have_ffmpeg():
        from pyglet.media.codecs import ffmpeg
        pyglet.media.add_decoders(ffmpeg)
    else:
        print("FFmpeg binaries could not be loaded.")


def _locate_binaries():
    """Locate the binaries depending on platform and architecture.

    Once binaries are correctly located, set the relevant environment
    variable to point to the binaries.

    On Windows this is PATH. On Mac OS this is LD_LIBRARY_PATH.
    """

    this_dir = os.path.abspath(os.path.dirname(__file__))

    if sys.platform == 'win32':
        is64bit = sys.maxsize > 2 ** 32

        if is64bit:
            path = os.path.join(this_dir, 'Win64')
        else:
            path = os.path.join(this_dir, 'Win32')

        env_var = 'PATH'

    elif sys.platform == 'darwin':
        path = os.path.join(this_dir, 'MacOS')
        env_var = 'LD_LIBRARY_PATH'
        pyglet.options['audio'] = ('openal', 'pulse', 'silent')

    paths = os.environ.get(env_var, '').split(os.pathsep)
    paths.append(path)
    os.environ[env_var] = os.pathsep.join(paths)
