from codecs import open
from os import path

from setuptools import setup, find_packages
from wheel.bdist_wheel import bdist_wheel

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

plat_pkg_data = {
    'win_amd64': ['Win64/*.dll'],
    'win32': ['Win32/*.dll'],
    'macosx_10_5_x86_64': ['MacOS/*.dylib'],
    'manylinux1_x86_64': ['linux_x86_64/*.so.*.*.*'],
    'linux-armv7l': ['RPi/*.so.*.*.*'],
}


class _bdist_wheels(bdist_wheel):
    def finalize_options(self):
        super().finalize_options()
        pkg_data = plat_pkg_data[self.plat_name]
        self.distribution.package_data = {'pyglet_ffmpeg': pkg_data}


setup(
    cmdclass={'bdist_wheel': _bdist_wheels},
    name='pyglet_ffmpeg',
    version='0.1.5',
    description='Platform wheels with ffmpeg binaries and ctypes for pyglet',
    long_description=long_description,
    url='https://github.com/pythonarcade/pyglet-ffmpeg',
    author='Daniel Gillet',
    author_email='dan.gillet737@gmail.com',
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
        'pyglet >= 1.4.0a1',
    ],
)
