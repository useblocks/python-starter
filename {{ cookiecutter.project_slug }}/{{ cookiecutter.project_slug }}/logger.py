import logging


def config_logger():
    log_format = "[%(levelname)5s] %(name)s - %(message)s"
    logging.basicConfig(format=log_format, level=logging.DEBUG)
