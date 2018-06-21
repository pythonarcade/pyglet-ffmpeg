from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyglet_ffmpeg',
    version='0.0.1.dev0',
    description='Platform wheels with ffmpeg binaries and ctypes for pyglet',
    long_description=long_description,
    url='https://github.com/pythonarcade/pyglet-ffmpeg',
    author='Daniel Gillet',
    author_email='TODO',  # TODO Daniel provide email
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Documentation',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='pyglet ffmpeg audio arcade',
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=[
        'pyglet',
    ],
)
