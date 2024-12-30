from unittest import TestCase


class TestExceptions(TestCase):
    def test_exceptions(self):
        from pyklatchat_utils.exceptions import KlatchatException, KlatAPIAuthorizationError, MalformedConfigurationException
        self.assertIsInstance(KlatchatException(), KlatchatException)
        self.assertIsInstance(KlatAPIAuthorizationError(), KlatchatException)
        self.assertIsInstance(MalformedConfigurationException(), KlatchatException)
