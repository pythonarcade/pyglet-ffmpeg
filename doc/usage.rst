Installation
============

.. warning::

    pyglet-ffmpeg currently only supports Windows (32 or 64 bits) and Mac OS X 10.5
    and above.

pyglet-ffmpeg bundles the binaries for FFmpeg v4. On PyPI, pyglet current stable
release (v1.3.2) does support FFmpeg at all. There is an unstable release (v1.4.0a1)
but it's using FFmpeg v3.

In order to make things work, you will need to install pyglet from Bitbucket
repository:

.. code-block:: bash

    $ pip install -e hg+https://bitbucket.org/pyglet/pyglet/branch/default#egg=pyglet

You install pyglet-ffmpeg using pip:

.. code-block:: bash

    $ pip install pyglet-ffmpeg

Usage
=====

Using pyglet-ffmpeg is really simple. In your code, simply call: ::

    import pyglet_ffmpeg
    pyglet_ffmpeg.load_ffmpeg()

FFmpeg will be loaded and ready to be used with pyglet or arcade.

Example using Pyglet
====================

Let's say you have an audio file `laser1.ogg` in the same directory as this script.
Here is a minimal example which would play the sound.

.. code-block:: python

    import pyglet
    import pyglet_ffmpeg
    from pathlib import Path

    pyglet_ffmpeg.load_ffmpeg()

    window = pyglet.window.Window()

    this_dir = Path(__file__).parent
    soundfile = str(this_dir / 'laser1.ogg')
    sound = pyglet.media.load(soundfile)
    player = sound.play()

    player.on_player_eos = window.close
    pyglet.app.run()