import unittest
from pda_cfg.pda import PushdownAutomaton


class TestBinaryPalindrome(unittest.TestCase):

    def setUp(self):
        self.pda = PushdownAutomaton()

    def test_valid_palindromes(self):
        self.assertTrue(self.pda.binary_palindrome("0"))
        self.assertTrue(self.pda.binary_palindrome("1"))
        self.assertTrue(self.pda.binary_palindrome("00"))
        self.assertTrue(self.pda.binary_palindrome("101"))
        self.assertTrue(self.pda.binary_palindrome("1001"))
        self.assertTrue(self.pda.binary_palindrome("01010"))

    def test_invalid_palindromes(self):
        self.assertFalse(self.pda.binary_palindrome("011"))
        self.assertFalse(self.pda.binary_palindrome("0100"))
        self.assertFalse(self.pda.binary_palindrome("102"))
        self.assertFalse(self.pda.binary_palindrome("abc"))


if __name__ == "__main__":
    unittest.main()