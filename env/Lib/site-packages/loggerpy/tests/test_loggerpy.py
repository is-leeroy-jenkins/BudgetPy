from unittest import TestCase

import loggerpy

class TestLogger(TestCase):
    def test_is_logger(self):
        logger = loggerpy.get_logger('test')
        self.assertTrue(isinstance(logger, loggerpy._Logger))