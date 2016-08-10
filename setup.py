#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
import novel
import sys

if __name__ == '__main__':
    assert sys.version_info.major > 2, 'Only works with python3'
    setup(
        name='FetchNovels',
        version=novel.__version__,
        description='Fetch novels from Internet',
        license='GPLv3',
        url='https://github.com/wangjiezhe/FetchNovels',

        author='wangjiezhe',
        author_email='wangjiezhe@gmail.com',

        packages=['novel', 'novel.sources', ],
        scripts=['fetchnovel.py', ],

        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Natural Language :: English',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
        ]
    )