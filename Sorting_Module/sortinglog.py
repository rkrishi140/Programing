import logging

my_logger = logging.getLogger(__name__)
my_logger.setLevel(logging.DEBUG)


formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

fileHandler = logging.FileHandler('Sort.log')
fileHandler.setFormatter(formatter)

my_logger.addHandler(fileHandler)