"""Test basic app functionality."""
from {{ cookiecutter.project_package }}.main import run


def test_run_main():
    """Check whether main function runs through."""
    run()
