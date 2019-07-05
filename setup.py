# coding: utf-8

import os
import codecs
from setuptools import setup, find_packages


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='tox-pipenv-install',
    description='Pipenv install plugin',
    long_description=read('README.rst'),
    version='0.1.0',
    author='Oleg Ermakov',
    author_email='ermakovolegs@gmail.com',
    maintainer='Oleg Ermakov',
    maintainer_email='ermakovolegs@gmail.com',
    url='https://github.com/ermakov-oleg/tox-pipenv-install',
    packages=find_packages(),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=['tox>=3.7.0'],
    entry_points={'tox': ['pipenv-install = tox_pipenv_install.plugin']},
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: tox',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
)
