import logging

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)
file_handler = logging.FileHandler('statistics.log')
file_handler.setFormatter(logging.Formatter('%(message)s'))
LOGGER.addHandler(file_handler)
