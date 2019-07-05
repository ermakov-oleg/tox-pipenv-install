# coding: utf-8
import sys

import pluggy


hook_impl = pluggy.HookimplMarker("tox")


@hook_impl
def tox_testenv_install_deps(venv, action):
    deps = venv.get_resolved_dependencies()
    if deps and 'pipenv' not in deps:
        deps.append('pipenv')
    else:
        deps = ['pipenv']

    depinfo = ", ".join(map(str, deps))
    action.setactivity("installdeps", depinfo)
    venv._install(deps, action=action)  # pylint: disable=protected-access

    basepath = venv.path.dirpath()
    basepath.ensure(dir=1)

    action.setactivity("installdeps", "pipenv install --dev")
    args = [sys.executable, "-m", "pipenv", "install", "--dev"]
    venv._pcall(args, venv=False, action=action, cwd=basepath)  # pylint: disable=protected-access

    return True
