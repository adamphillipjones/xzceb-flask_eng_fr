import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglish(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(englishToFrench('Helo'),'Hello')
        self.assertEqual(englishToFrench('Hello'),'Bonjour')

class TestFrench(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(frenchToEnglish('Bonjour'),'Bonjour')
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')

unittest.main()