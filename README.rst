pyglet-ffmpeg
=============

Provide binary wheels for using ffmpeg with pyglet on certain platforms.

Background
==========

`pyglet <https://bitbucket.org/pyglet/pyglet/wiki/Home>`_ is a popular
Python package for writing OpenGL applications.
`Arcade <http://arcade.academy>`_ is an easy-to-learn Python library for
creating 2D video games.

pyglet traditionally used AVbin for sound, but AVbin has issues.
Recent work has focused on having pyglet instead support
`fmpeg <https://www.ffmpeg.org>`_, a cross-platform, open source
library for video and audio. But pyglet doesn't ship binaries, which
means Arcade users and developers need to install ffmpeg themselves.

This package aims to solve this. It provides platform-dependent wheels
on supported operating systems for using ffmpeg in pyglet, bundling
the ffmpeg binaries.

*Note: Windows and Mac are initially supported.*

Installation
============

TODO

Developing
==========

TODO

