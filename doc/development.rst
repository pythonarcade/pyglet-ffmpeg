Development
===========

Want to work on ``pyglet_ffmpeg``? This document explains how to get a
working sandbox, make releases, and some of the decisions made for
good housekeeping.

Sphinx
======

This project uses Sphinx for documentation. The docs are hosted on
ReadTheDocs, connected by the RTD/GitHub integration. Local docs
generation uses the ``sphinx_rtd_theme`.

Testing
=======

This project uses ``pytest``. The tests are under ``tests``, with
directories for unit test and other kinds of test. We also use
``pytest-mock`` and ``pytest-cov``.

Run tests with coverage from the command line with the following,
done from the root directory:

.. code-block:: bash

  $ pytest --cov=pyglet_ffmpeg tests
