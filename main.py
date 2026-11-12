# SRM FLA ASSESSMENT TASK 3
# PDA AND CFG CASE STUDY APPLICATION

from balanced_parentheses import run_balanced, test_balanced
from arithmetic_expression import run_arithmetic, test_arithmetic
from palindrome_checker import run_palindrome, test_palindrome


def main():

    while True:

        print("\n" + "=" * 55)
        print("       CASE STUDY BASED ANALYSIS AND DESIGN")
        print("                  USING PDA AND CFG")
        print("=" * 55)

        print("\n1. Balanced Parentheses Checker")
        print("2. Arithmetic Expression Validator")
        print("3. Palindrome Checker")
        print("4. Run All Test Cases")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            run_balanced()

        elif choice == "2":
            run_arithmetic()

        elif choice == "3":
            run_palindrome()

        elif choice == "4":

            print("\n===== AUTOMATED TESTING =====")

            test_balanced()
            test_arithmetic()
            test_palindrome()

            print("\nALL TEST CASES COMPLETED")

        elif choice == "5":
            print("\nThank you for using the application!")
            break

        else:
            print("\nInvalid choice. Try again.")


if __name__ == "__main__":
    main()