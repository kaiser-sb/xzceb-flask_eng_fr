import unittest
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    """
    Test translator functions
    """
    def test_english_to_french(self):
        """
        Test English to French function
        """
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("Thanks"), "Merci")
        self.assertNotEqual(english_to_french(" "), "Rien")

    def test_french_to_english(self):
        """
        Test French to English function
        """
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Bien"), "Good")
        self.assertNotEqual(french_to_english(" "), "None")

unittest.main()


