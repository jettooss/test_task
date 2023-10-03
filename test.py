import json
import os
import unittest

from main import program_start
class TestProcessDataNew(unittest.TestCase):


    def setUp(self):
        # Writing the files for testing
        # messages data
        messages_data = [
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

        with open('pdata.json', 'w') as f:
            json.dump(messages_data, f)

        # replacements data
        replacements = [
            {"replacement": "Joyful! I've outsmarted you!", "source": "I wondered whether I should return"},
            {"replacement": "akfhjksahf skjfghsidgh ijgfiwghfg", "source": "Ages and ages ago:"},
            {"replacement": "9", "source": "y"},
            {"replacement": "All is silent... or is it?", "source": None},
            {"replacement": "f12324344sss6g9gdf2dbdb", "source": "tree"},
            {"replacement": "Arbitrary script, for sure", "source": "grabbed"},
            {"replacement": "Ramble-ramble-ramble, just a bunch of LETTERS", "source": None},
            {"replacement": "parenthesis - a term of intellect", "source": "the superior option"},
            {"replacement": "Absolutely vacant... or is it?", "source": "Have roamed"},
            {"replacement": "Scooby-Doo, where are you?", "source": "realizing that path leads on"},
            {"replacement": "Another cryptic message", "source": None},
            {"replacement": "Scooby-Doo, where are you?", "source": "realizing that path mediates"}
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

        with open('preplacement.json', 'w') as f:
            json.dump(replacements, f)

    def test_process_data_new(self):
        program_start('pdata.json', 'preplacement.json', 'test1.json')
        with open("test1.json", "r") as f:
            output_data = json.load(f)

        self.assertEqual(output_data, self.expected_output_data)

    def tearDown(self):
        os.remove('pdata.json')
        os.remove('preplacement.json')
[]
if __name__ == "__main__":
  unittest.main()