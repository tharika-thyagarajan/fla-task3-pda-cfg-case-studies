import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from pda_cfg.pda import PushdownAutomaton
from pda_cfg.parser import ArithmeticExpressionParser

pda = PushdownAutomaton()
parser = ArithmeticExpressionParser()

tests = {
    "Balanced Parentheses": [
        ("()", True),
        ("(())", True),
        ("{[()]}", True),
        ("(()", False),
        ("([)]", False)
    ],
    "Arithmetic Expressions": [
        ("a+b", True),
        ("2+3*4", True),
        ("(5+2)*3", True),
        ("a+", False),
        ("5+*3", False)
    ],
    "Binary Palindrome": [
        ("101", True),
        ("1001", True),
        ("01010", True),
        ("011", False),
        ("0100", False)
    ]
}

functions = {
    "Balanced Parentheses": pda.balanced_parentheses,
    "Arithmetic Expressions": parser.validate,
    "Binary Palindrome": pda.binary_palindrome
}

total = 0
passed = 0

print("=" * 55)
print("          AUTOMATED TESTING REPORT")
print("=" * 55)

for category, cases in tests.items():
    print("\n", category)
    print("-" * 40)

    for value, expected in cases:
        actual = functions[category](value)
        status = "PASS" if actual == expected else "FAIL"

        print(f"{value!r:15} Expected: {expected}  Result: {status}")

        total += 1
        if actual == expected:
            passed += 1

print("\n" + "=" * 55)
print(f"TOTAL TESTS: {total}")
print(f"PASSED: {passed}")
print(f"FAILED: {total - passed}")
print("=" * 55)

if passed == total:
    print("ALL TESTS PASSED SUCCESSFULLY!")
else:
    print("SOME TESTS NEED CORRECTION.")