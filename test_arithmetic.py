import unittest
from pda_cfg.parser import ArithmeticExpressionParser


class TestArithmeticExpression(unittest.TestCase):

    def setUp(self):
        self.parser = ArithmeticExpressionParser()

    def test_valid_expressions(self):
        self.assertTrue(self.parser.validate("a+b"))
        self.assertTrue(self.parser.validate("2+3*4"))
        self.assertTrue(self.parser.validate("(5+2)*3"))
        self.assertTrue(self.parser.validate("12*(x+3)"))
        self.assertTrue(self.parser.validate("-5+2"))

    def test_invalid_expressions(self):
        self.assertFalse(self.parser.validate("a+"))
        self.assertFalse(self.parser.validate("a**b"))
        self.assertFalse(self.parser.validate("(a+b"))
        self.assertFalse(self.parser.validate("5+*3"))
        self.assertFalse(self.parser.validate(""))

if __name__ == "__main__":
    unittest.main()