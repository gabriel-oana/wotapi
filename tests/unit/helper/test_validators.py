import unittest

from wotapi.helper.validators import Validators


class TestValidators(unittest.TestCase):

    def test_check_parameters(self):
        result = Validators.check_if_param_exists("param1", "param2")
        expected = True
        self.assertEqual(result, expected)

    def test_wrong_parameters(self):
        self.assertRaises(ValueError, Validators.check_if_param_exists, "1", None)

    def test_wrong_parameter_type(self):
        self.assertRaises(ValueError, Validators.check_if_param_exists, None, "1")

    def test_wrong_realm(self):
        self.assertRaises(ValueError, Validators.check_realm, "some_garbage")

    def test_correct_realm(self):
        response = Validators.check_realm("eu")
        expected = True
        self.assertEqual(response, expected)
