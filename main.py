from pda_cfg.pda import PushdownAutomaton
from pda_cfg.parser import ArithmeticExpressionParser


def main():
    pda = PushdownAutomaton()
    parser = ArithmeticExpressionParser()

    while True:
        print("\n" + "=" * 55)
        print("       CASE STUDY BASED ANALYSIS AND DESIGN")
        print("                    USING PDA AND CFG")
        print("=" * 55)

        print("\n1. Balanced Parentheses Checker")
        print("2. Arithmetic Expression Validator")
        print("3. Binary Palindrome Checker")
        print("4. Run All Test Cases")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            expression = input("Enter parentheses expression: ")

            if pda.balanced_parentheses(expression):
                print("Result: ACCEPTED")
            else:
                print("Result: REJECTED")

        elif choice == "2":
            expression = input("Enter arithmetic expression: ")

            if parser.validate(expression):
                print("Result: ACCEPTED")
            else:
                print("Result: REJECTED")

        elif choice == "3":
            string = input("Enter binary string: ")

            if pda.binary_palindrome(string):
                print("Result: ACCEPTED")
            else:
                print("Result: REJECTED")

        elif choice == "4":
            print("\n========== AUTOMATED TESTING ==========")

            balanced_tests = [
                ("()", True),
                ("(())", True),
                ("{[()]}", True),
                ("(()", False),
                ("())", False)
            ]

            arithmetic_tests = [
                ("a+b", True),
                ("2+3*4", True),
                ("(5+2)*3", True),
                ("a+", False),
                ("5+*3", False)
            ]

            palindrome_tests = [
                ("0", True),
                ("101", True),
                ("1001", True),
                ("01010", True),
                ("011", False),
                ("0100", False)
            ]

            print("\nBALANCED PARENTHESES TEST CASES")
            for value, expected in balanced_tests:
                result = pda.balanced_parentheses(value)
                print(value, ":", "Accepted" if result else "Rejected")

            print("\nARITHMETIC EXPRESSION TEST CASES")
            for value, expected in arithmetic_tests:
                result = parser.validate(value)
                print(value, ":", "Accepted" if result else "Rejected")

            print("\nBINARY PALINDROME TEST CASES")
            for value, expected in palindrome_tests:
                result = pda.binary_palindrome(value)
                print(value, ":", "Accepted" if result else "Rejected")

            print("\nALL TEST CASES COMPLETED")

        elif choice == "5":
            print("\nThank you! Program terminated.")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()