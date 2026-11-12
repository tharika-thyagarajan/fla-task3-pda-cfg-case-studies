# FLA TASK 3 - CASE STUDY 1
# BALANCED PARENTHESES CHECKER USING PDA

def balanced_pda(expression):

    stack = []
    matching = {')': '(', ']': '[', '}': '{'}

    for char in expression:

        if char in "([{":
            stack.append(char)

        elif char in ")]}":

            if not stack:
                return False, "No matching opening bracket"

            if stack[-1] == matching[char]:
                stack.pop()
            else:
                return False, "Mismatched brackets"

        else:
            return False, "Invalid character"

    if not stack:
        return True, "All brackets are balanced"

    return False, "Unmatched opening brackets"


def run_balanced():

    print("\n===== BALANCED PARENTHESES CHECKER =====")
    print("Supported brackets: (), [], {}")

    expression = input("Enter expression: ")

    result, message = balanced_pda(expression)

    print("\nRESULT:", "ACCEPTED" if result else "REJECTED")
    print("Explanation:", message)


def test_balanced():

    accepted = ["()", "(())", "{[()]}", "()[]{}", "(([]){})"]
    rejected = ["(", "([)]", "(()", "[(])", ")"]

    print("\nBALANCED PARENTHESES TEST CASES")

    for item in accepted:
        result, _ = balanced_pda(item)
        print(item, ":", "Accepted" if result else "FAILED")

    for item in rejected:
        result, _ = balanced_pda(item)
        print(item, ":", "Rejected" if not result else "FAILED")