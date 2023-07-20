import unittest
from tenloc import tenloc


class TestStub(unittest.TestCase):

    def test_parser(self):
        # Given
        input = ["--name", "Davo"]

        # When
        result = tenloc.setup(input)

        # Then
        self.assertFalse(result.verbose)
        self.assertEqual(result.name, input[1])

    def test_no_name(self):
        # When
        result = tenloc.run()

        # Then
        self.assertEqual(result, "Hello, world!")

    def test_name(self):
        # When
        result = tenloc.run("Davo")

        # Then
        self.assertEqual(result, "Hello, Davo!")
