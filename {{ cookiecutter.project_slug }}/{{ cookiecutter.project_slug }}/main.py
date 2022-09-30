"""Entry point to the app."""

import logging

from {{ cookiecutter.project_slug }}.logger import config_logger


logger = logging.getLogger(__name__)


def run():
    config_logger()
    logger.info("This program should have never been built.")


if __name__ == "__main__":
    run()
