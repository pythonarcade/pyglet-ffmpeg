Development
===========

Want to work on ``pyglet_ffmpeg``? This document explains how to get a
working sandbox, make releases, and some of the decisions made for
good housekeeping.

Sphinx
======

This project uses Sphinx for documentation. The docs are hosted on
ReadTheDocs, connected by the RTD/GitHub integration. Local docs
generation uses the ``sphinx_rtd_theme``.

Testing
=======

This project uses ``pytest``. The tests are under ``tests``, with
directories for unit test and other kinds of test. We also use
``pytest-mock`` and ``pytest-cov``.

Run tests with coverage from the command line with the following,
done from the root directory:

.. code-block:: bash

  $ pytest --cov=pyglet_ffmpeg tests

Version Numbering
=================

This project uses semantic versioning. To ensure the scheme is enforced
and to update all locations of the version number (setup.py, doc/conf.py,
pyglet_ffmpeg/__init__.py), we use
`bump2version <https://github.com/c4urself/bump2version>`_ to set our version
numbers.

Bump the version using
`bump2version commands <https://github.com/peritus/bump2version/issues/77#issuecomment-130696156>`_:

- `bump2version patch: 0.1.0 -> 0.1.1.dev0`

- `bump2version release: 0.1.1.dev0 -> 0.1.1`

- `bump2version minor: 0.1.1 -> 0.2.0.dev0`

- `bump2version dev: 0.2.0.dev0 -> 0.2.0.dev1`

- `bump2version release: 0.2.0.dev1 -> 0.2.0#. Tag the release.`

It's a little bit of a hassle but better than doing it manually.

Also, we set the ``bump2version`` config file to automatically tag
and commit.

PyPI
====

Releases are pushed to PyPI from Travis, using the
`regular TravisCI-PyPI scheme <https://docs.travis-ci.com/user/deployment/pypi/>`_.
A push to a tag triggers not just the rest of the Travis build, but also the
upload to PyPI of the new version...hands-free, from Travis.

Compiling FFmpeg for Ubuntu
===========================

To make new binaries for Ubuntu, here are the required steps:

.. code-block:: bash

    sudo apt-get update -qq && sudo apt-get -y install \
      autoconf \
      automake \
      build-essential \
      cmake \
      git-core \
      libtool \
      pkg-config \
      texinfo \
      wget \
      zlib1g-dev \
      yasm

    mkdir -p ~/ffmpeg_sources ~/bin

    cd ~/ffmpeg_sources && \
    wget https://www.nasm.us/pub/nasm/releasebuilds/2.13.03/nasm-2.13.03.tar.bz2 && \
    tar xjvf nasm-2.13.03.tar.bz2 && \
    cd nasm-2.13.03 && \
    ./autogen.sh && \
    PATH="$HOME/bin:$PATH" ./configure --prefix="$HOME/ffmpeg_build" --bindir="$HOME/bin" && \
    make && \
    make install

    cd ~/ffmpeg_sources && \
    wget https://nixos.org/releases/patchelf/patchelf-0.9/patchelf-0.9.tar.bz2 && \
    tar xjvf patchelf-0.9.tar.bz2 && \
    cd patchelf-0.9 && \
    autoreconf --verbose --install --force --warnings=all && \
    PATH="$HOME/bin:$PATH" ./configure --prefix="$HOME/ffmpeg_build" --bindir="$HOME/bin" && \
    make && \
    make install

    cd ~/ffmpeg_sources && \
    wget -O ffmpeg-snapshot.tar.bz2 https://ffmpeg.org/releases/ffmpeg-snapshot.tar.bz2 && \
    tar xjvf ffmpeg-snapshot.tar.bz2 && \
    cd ffmpeg && \
    PATH="$HOME/bin:$PATH" PKG_CONFIG_PATH="$HOME/ffmpeg_build/lib/pkgconfig" ./configure \
      --prefix="$HOME/ffmpeg_build" \
      --extra-cflags="-I$HOME/ffmpeg_build/include" \
      --extra-ldflags="-L$HOME/ffmpeg_build/lib" \
      --extra-libs="-lpthread -lm" \
      --bindir="$HOME/bin" \
      --disable-programs \
      --disable-doc \
      --disable-static \
      --enable-shared \
      --disable-avdevice \
      --disable-postproc && \
    PATH="$HOME/bin:$PATH" make && \
    make install && \
    hash -r

This will create the needed so files in `~/ffmpeg_build/lib`. Move into this directory
and use `patchelf` to add relative path to each **so** file so they can load their
dependencies.

.. code-block:: bash

    for file in *.so.*.*;
        do ~/bin/patchelf --set-rpath \$ORIGIN "$file";
    done;


You can now copy those files to the ``linux_x86_64`` folder in pyglet-ffmpeg package.

.. warning::

    Only copy the libraries, not the symlinks. The compilation step will have created
    for instance a file named ``libavcodec.so.58.21.104``, but there will be two 
    symlinks named ``libavcodec.so.58`` and ``libavcodec.so``. Only copy
    ``libavcodec.so.58.21.104``. The package will re-create the correct symlinks when
    running, but only if the symlinks are **not** initially present.
