Introduction
============

``Python-Starter`` is an opiniated `Cookiecutter <https://github.com/cookiecutter/cookiecutter>`_ recipe for new
Python projects.
Created in 2022, hope is not yet abandoned it is still relevant in future.

It cares for your mental load by reducing configuration options.

✨ **Features**

- 📝 Project metadata via
  `pyproject.toml <https://python-poetry.org/docs/pyproject/>`_ and
  `Poetry <https://python-poetry.org/>`_
- 📜 Continuous documentation via `Sphinx <https://github.com/sphinx-doc/sphinx/>`_ and 
  `Read the Docs <https://github.com/readthedocs/readthedocs.org>`_
- 🧮 Changelog via `Keep a Changelog <https://keepachangelog.com>`_
- ⚫ Formatting via `Black <https://github.com/psf/black>`_
- 🔀 Import sorting via `isort <https://github.com/PyCQA/isort>`_
- ⏰ Fast `pre-commit <https://github.com/pre-commit/pre-commit>`_ setup
- 🦈 Linting with `flake8 <https://github.com/pycqa/flake8>`_ and `pylint <https://github.com/PyCQA/pylint>`_
- 🛡 Type checking with `mypy <https://github.com/python/mypy>`_
- ✅ Tests via `pytest <https://github.com/pytest-dev/pytest/>`_ and `Nox <https://github.com/wntrblm/nox>`_
- 🔄 CI via `Github actions <https://github.com/features/actions>`_ on Linux and Windows
- ⚡ Auto deploy to `PyPI <https://pypi.org/>`_
- 🔨 Complete IDE setup for `VS Code <https://github.com/Microsoft/vscode>`_
- 🚫 `.gitignore <https://git-scm.com/docs/gitignore>`_ setup
- 🕺 Authors file
- ⠻ Python `logging <https://docs.python.org/3/library/logging.html>`_ setup

Usage
=====

1. Install cookiecutter::

    pip install cookiecutter

2. Run it::
    
    cookiecutter gh:useblocks/python-starter
