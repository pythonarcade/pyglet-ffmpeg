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
`bumpversion <https://github.com/peritus/bumpversion>`_ to set our version
numbers.

Bump the version using
`bumpversion commands <https://github.com/peritus/bumpversion/issues/77#issuecomment-130696156>`_:

- `bumpversion patch: 0.1.0 -> 0.1.1.dev0`

- `bumpversion release: 0.1.1.dev0 -> 0.1.1`

- `bumpversion minor: 0.1.1 -> 0.2.0.dev0`

- `bumpversion dev: 0.2.0.dev0 -> 0.2.0.dev1`

- `bumpversion release: 0.2.0.dev1 -> 0.2.0#. Tag the release.`

It's a little bit of a hassle but better than doing it manually.

Changelog
=========

The changelog is an important part of documentation. We use the Python package
`gitchangelog <https://github.com/vaab/gitchangelog>`_ to generate a readable,
organized changelog from git information. This is written into ``CHANGES.rst``
(alas, after a commit...as it needs the change information in the history.)

PyPI
====

Releases are pushed to PyPI from Travis, using the
`regular TravisCI-PyPI scheme <https://docs.travis-ci.com/user/deployment/pypi/>`_.
A push to master triggers not just the rest of the Travis build, but also the
upload to PyPI of the new version...hands-free, from Travis.

Dev/Release Process
===================

Thus, the dev/release process works a little something like this:

- Make a branch

- Run ``bumpversion dev``

- Finish work, merge to master, commit

- Run ``bumpversion release``

- Commit, tag

- Run ``gitchangelog > CHANGES.rst``

- Commit, push with tags
