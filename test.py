
import os
import unittest
import json

from main import program_start


class TestProcessDataNew(unittest.TestCase):

    def setUp(self):
        """Setting up test files"""
        self.messages_data = [
                            "Two routes diverged in a pale f12324344sss6g9gdf2dbdb,",
                            "Author Ice Frost poetAnd sorry I could not travel both",
                            "Another cryptic message",
                            "And be a single traveler, standing for a while",
                            "And viewed one as far as I could",
                            "Ramble-ramble-ramble, just a bunch of LETTERS",
                            "To where it took a turn in the undergrowth;",
                            "Then Arbitrary script, for surely the other, as equally lovely,",
                            "And having perhaps parenthesis - a term of intellect,",
                            "Ramble-ramble-ramble, just a bunch of LETTERS",
                            "Because it was leafy and desired wandering;",
                            "Another cryptic message",
                            "Another cryptic message",
                            "Although as for that the wandering there",
                            "Absolutely vacant... or is it? them really nearly identical,",
                            "And both in the morning light lay",
                            "In leaves no foot had changed to black.",
                            "Oh, I saved the first for another time!",
                            "But Scooby-Doo, where are you? route mediates the way,",
                            "Joyful! I've outsmarted you!",
                            "Another cryptic message",
                            "I will be recounting this with a hint of regret",
                            "akfhjksahf skjfghsidgh ijgfiwghfg",
                            "Two routes diverged in a f12324344sss6g9gdf2dbdb, and I",
                            "I Arbitrary script, for surely the one less followed by,",
                            "And that has altered all the difference.",
                            "Ramble-ramble-ramble, just a bunch of LETTERS"
                    ]

        self.replacements_with_source = [
            {"replacement": "Joyful! I've outsmarted you!", "source": "I wondered whether I should return"},
            {"replacement": "akfhjksahf skjfghsidgh ijgfiwghfg", "source": "Ages and ages ago:"},
            {"replacement": "9", "source": "y"},
            {"replacement": "f12324344sss6g9gdf2dbdb", "source": "tree"},
            {"replacement": "Arbitrary script, for sure", "source": "grabbed"},
            {"replacement": "parenthesis - a term of intellect", "source": "the superior option"},
            {"replacement": "Absolutely vacant... or is it?", "source": "Have roamed"},
            {"replacement": "Scooby-Doo, where are you?", "source": "realizing that path leads on"},
            {"replacement": "Scooby-Doo, where are you?", "source": "realizing that path mediates"}
        ]

        self.replacements_without_source = [
            {"replacement": "All is silent... or is it?", "source": None},
            {"replacement": "Ramble-ramble-ramble, just a bunch of LETTERS", "source": None},
            {"replacement": "Another cryptic message", "source": None}
        ]
        self.expected_output_data = [
                    "Two routes diverged in a pale tree,",
                    "Then grabbedly the other, as equally lovely,",
                    "And having perhaps the superior option,",
                    "Have roamed them really nearly identical,",
                    "But realizing that path leads on route mediates the way,",
                    "I wondered whether I should return",
                    "Ages and ages ago:",
                    "Two routes diverged in a tree, and I",
                    "I grabbedly the one less followed by,"
                ]

        self._write_json_to_file(self.messages_data, 'pdata.json')


    def test_replacements_with_source(self):
        with open('preplacement.json', 'w') as f:
            json.dump(self.replacements_with_source, f)

        program_start('pdata.json', 'preplacement.json', 'test1.json')


        os.remove('preplacement.json')



    def _write_json_to_file(self, data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f)

    def _run_and_test_program(self, replacements, output_filename):
        self._write_json_to_file(replacements, 'preplacement.json')

        # Assuming your program_start function returns the processed data
        output_data = program_start('pdata.json', 'preplacement.json', output_filename)
        # print(output_data)
        os.remove('preplacement.json')

        return output_data

    def test_replacements_with_source(self):
        self._run_and_test_program(self.replacements_with_source, "test1.json")

    def test_replacements_without_source(self):
        self._run_and_test_program(self.replacements_without_source, "test2.json")

    def test_process_data_new(self):
        combined_replacements = self.replacements_with_source + self.replacements_without_source
        output_data = self._run_and_test_program(combined_replacements, "test3.json")
        expected_data = self.expected_output_data

        self.assertEqual(output_data, expected_data)
    def tearDown(self):
        os.remove('pdata.json')

if __name__ == "__main__":
    unittest.main()