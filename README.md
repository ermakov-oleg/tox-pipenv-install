# tox-pipenv-install

[![PyPI version](https://img.shields.io/pypi/v/tox-pipenv-install.svg)](https://pypi.org/project/tox-pipenv-install) [![Python
versions](https://img.shields.io/pypi/pyversions/tox-pipenv-install.svg)](https://pypi.org/project/tox-pipenv-install) [![See Build Status on Travis
CI](https://travis-ci.org/ermakov-oleg/tox-pipenv-install.svg?branch=master)](https://travis-ci.org/ermakov-oleg/tox-pipenv-install) [![codecov](https://codecov.io/gh/ermakov-oleg/tox-pipenv-install/branch/master/graph/badge.svg)](https://codecov.io/gh/ermakov-oleg/tox-pipenv-install)

-----

## Features

* Easy installation of package dependencies from `Pipfile` and `Pipfile.lock`
* Dependencies are installed only once, when creating an environment (to recreate use `tox -r`)


## Installation

You can install "tox-pipenv-install" via
[pip](https://pypi.org/project/pip/) from [PyPI](https://pypi.org):

    $ pip install tox-pipenv-install

## Usage

#### Example:

Simple `tox.ini` file using pipenv to install dependencies:

```ini
[tox]
envlist = py36

[testenv]
deps =
    pipenv
commands =
  pipenv install --dev
  pytest ..
```

After plugin installation:

```ini
[tox]
envlist = py36

[testenv]
commands =
  pytest ..
```
The plugin implicitly installs `pipenv` and runs `pipenv install --dev`

## Contributing

Contributions are very welcome. Tests can be run with
[tox](https://tox.readthedocs.io/en/latest/), please ensure the coverage
at least stays the same before you submit a pull request.

## License

Distributed under the terms of the
[MIT](http://opensource.org/licenses/MIT) license, "tox-pipenv-install"
is free and open source software

## Issues

If you encounter any problems, please [file an
issue](https://github.com/ermakov-oleg/tox-pipenv-install/issues) along
with a detailed description.