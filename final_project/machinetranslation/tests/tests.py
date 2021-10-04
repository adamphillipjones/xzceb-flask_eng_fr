
import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(''), '') # Test null input
        self.assertEqual(english_to_french('Hello', 'Bonjour')) # Test Hello and compare to expected Bonjour

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(''), '') # Test null input
        self.assertEqual(french_to_english('Bonjour', 'Hello')) # Test Bonjour and compare to expected Hello

unittest.main()