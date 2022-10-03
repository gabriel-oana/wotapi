import unittest

from wotapi.helper.logger import create_logger


class TestLogger(unittest.TestCase):

    def test_logger(self):
        logger = create_logger(log_level='INFO')
        logger.info('TESTING')

