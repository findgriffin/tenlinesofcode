import unittest
from unittest.mock import patch

from tenloc import tenloc


class TestStub(unittest.TestCase):

    def test_parser(self):
        # Given
        input = ["--all"]

        # When
        result = tenloc.setup(input)

        # Then
        self.assertFalse(result.verbose)
        self.assertTrue(result.all)

    def test_no_name(self):
        # When
        result = tenloc.run(tenloc.setup([]))

        # Then
        self.assertIsNone(result)

    def test_say_my_name(self):
        # When
        with patch('builtins.input', return_value='Davo'):
            result = tenloc.run(tenloc.setup(['say_my_name']))
            # Then
            self.assertIsNone(result)

    def test_metronome(self):
        tenloc.run(tenloc.setup(['metronome']), testing=True)
