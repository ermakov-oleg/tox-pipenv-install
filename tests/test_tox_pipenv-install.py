# coding: utf-8
from tox.venv import tox_testenv_create

from tox_pipenv_install.plugin import tox_testenv_install_deps


def test_install_deps_indexserver__with_deps(newmocksession):
    mocksession = newmocksession(
        [],
        """\
        [tox]
        [testenv:py123]
        deps=
            dep1
        """,
    )
    venv = mocksession.getvenv("py123")
    with mocksession.newaction(venv.name, "getenv") as action:
        tox_testenv_create(action=action, venv=venv)
        pcalls = mocksession._pcalls
        assert len(pcalls) == 1
        pcalls[:] = []

        tox_testenv_install_deps(action=action, venv=venv)

        assert len(pcalls) == 2
        args = " ".join(pcalls[0].args)
        assert args.endswith('-m pip install dep1 pipenv')

        args = " ".join(pcalls[1].args)
        assert args.endswith('-m pipenv install --dev')


def test_install_deps_indexserver__without_deps(newmocksession):
    mocksession = newmocksession(
        [],
        """\
        [tox]
        [testenv:py123]
        """,
    )
    venv = mocksession.getvenv("py123")
    with mocksession.newaction(venv.name, "getenv") as action:
        tox_testenv_create(action=action, venv=venv)
        pcalls = mocksession._pcalls
        assert len(pcalls) == 1
        pcalls[:] = []

        tox_testenv_install_deps(action=action, venv=venv)

        assert len(pcalls) == 2
        args = " ".join(pcalls[0].args)
        assert args.endswith('-m pip install pipenv')

        args = " ".join(pcalls[1].args)
        assert args.endswith('-m pipenv install --dev')
