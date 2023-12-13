import contextlib
import os
import string
import unittest
from unittest.mock import patch

from tenloc import tenloc
from tenloc.matrix import matrix_frames
from tenloc.pretty_json import pretty_json_files
from tenloc.spinner import spin


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

class TestMatrix(unittest.TestCase):

    def test_matrix_frames(self):
        frames = matrix_frames(4, string.ascii_lowercase, 2, 0.0)
        self.assertEqual(len(frames), 4)

class TestPrettyJSON(unittest.TestCase):
    JSON_FILE = 'tests/empty.json'
    GIT_IGNORE = '.gitignore'

    def test_pretty_json(self):
        pretty_json_files(['doesnotexist', self.JSON_FILE, self.GIT_IGNORE])

    @classmethod
    def tearDownClass(cls):
        pretty_file = cls.JSON_FILE.replace('.json', '-pretty.json')
        with contextlib.suppress(FileNotFoundError):
            os.remove(pretty_file)


class TestSpinner(unittest.TestCase):

    def test_spinner(self):
        spin(['-', '|'])
