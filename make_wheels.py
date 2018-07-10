#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import subprocess
import shutil

platforms = ['win_amd64', 'win32', 'macosx_10_5_x86_64', 'manylinux1_x86_64']

if __name__ == '__main__':
    for platform in platforms:
        print('-' * 60)
        print("Creating wheel for", platform)
        shutil.rmtree('build', ignore_errors=True)
        subprocess.run(['python', 'setup.py', 'bdist_wheel', '-p', platform])
