import unittest

from  unique_morse_code_words import uniqueMorseRepresentations


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

class WordCountTests(unittest.TestCase):

    def test_count_one_word(self):
        self.assertEqual(
            uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]),
            2
        )


if __name__ == '__main__':
    unittest.main()