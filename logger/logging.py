import logging


def configure_logging():
    logging.basicConfig(filename='download.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def get_logger():
    return logging.getLogger(__name__)
