import unittest
from unittest.mock import patch
from wotapi.action.base_action import BaseAction


class TestBaseAction(unittest.TestCase):

    def test_class_raises(self):
        self.assertRaises(TypeError, BaseAction)

    @patch.multiple(BaseAction, __abstractmethods__=set())
    def test_etl_data_raises(self):
        b = BaseAction()
        self.assertRaises(NotImplementedError, b.etl_data, application_id='test')