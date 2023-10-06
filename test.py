
import os
import unittest
import json

from main import program_start
#
#

class TestProcessDataNew(unittest.TestCase):

    def test_process_data_thewhite(self):
        actual_output=program_start('data.json', 'replacement.json', 'output1.json')
        expected_output = self.load_data_from_file('initial-data.json')
        self.assertEqual(actual_output, expected_output)

    def test_process_data_new(self):
        actual_output=program_start('my_data.json', 'replace.json', 'output2.json')
        expected_output = self.load_data_from_file('expected_output_data.json')
        self.assertEqual(actual_output, expected_output)

    def load_data_from_file(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        return data



if __name__ == "__main__":
    unittest.main()


