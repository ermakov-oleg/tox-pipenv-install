# -*- coding: utf-8 -*-
import logging
import sys

import pluggy


hookimpl = pluggy.HookimplMarker("tox")

log = logging.getLogger('pipenv-install')


@hookimpl
def tox_testenv_install_deps(venv, action):
    deps = venv.get_resolved_dependencies()
    if deps:
        if 'pipenv' not in deps:
            deps.append('pipenv')

        depinfo = ", ".join(map(str, deps))
        action.setactivity("installdeps", depinfo)
        venv._install(deps, action=action)

    basepath = venv.path.dirpath()
    basepath.ensure(dir=1)

    action.setactivity("installdeps", "pipenv install --dev")
    args = [sys.executable, "-m", "pipenv", "install", "--dev"]
    venv._pcall(args, venv=False, action=action, cwd=basepath)

    return True
