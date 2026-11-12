import unittest
from pda_cfg.pda import PushdownAutomaton


class TestBalancedParentheses(unittest.TestCase):

    def setUp(self):
        self.pda = PushdownAutomaton()

    def test_valid_parentheses(self):
        self.assertTrue(self.pda.balanced_parentheses("()"))
        self.assertTrue(self.pda.balanced_parentheses("(())"))
        self.assertTrue(self.pda.balanced_parentheses("{[()]}"))

    def test_invalid_parentheses(self):
        self.assertFalse(self.pda.balanced_parentheses("(()"))
        self.assertFalse(self.pda.balanced_parentheses("())"))
        self.assertFalse(self.pda.balanced_parentheses("([)]"))


if __name__ == "__main__":
    unittest.main()