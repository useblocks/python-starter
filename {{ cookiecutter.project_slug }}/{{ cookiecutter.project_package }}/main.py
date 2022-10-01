"""Entry point to the app."""

import logging

from {{ cookiecutter.project_package }}.logger import config_logger


logger = logging.getLogger(__name__)


def run() -> None:
    config_logger()
    logger.info("This program should have never been built.")


if __name__ == "__main__":
    run()
