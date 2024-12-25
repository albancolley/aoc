import logging


def configure(log_level="INFO"):
    logging.basicConfig(encoding='utf-8', level=logging.DEBUG)