# FLA TASK 3 - CASE STUDY 3
# PALINDROME CHECKER USING NPDA

def simulate_branch(text, midpoint, odd_length):

    stack = []
    trace = []

    first_half = text[:midpoint]

    # Q0: Push first half
    for char in first_half:
        stack.append(char)
        trace.append("Q0: PUSH " + char)

    # Q0 -> Q1: Guess the midpoint
    if odd_length:
        trace.append("Q0 -> Q1: Skip middle symbol " + text[midpoint])
        remaining = text[midpoint + 1:]
    else:
        trace.append("Q0 -> Q1: Even midpoint")
        remaining = text[midpoint:]

    # Q1: Match and pop
    for char in remaining:

        if not stack:
            return False, trace

        if stack[-1] == char:
            stack.pop()
            trace.append("Q1: POP " + char)
        else:
            trace.append("Q1: Mismatch")
            return False, trace

    # Q2: Accept
    if not stack:
        trace.append("Q2: ACCEPT")
        return True, trace

    return False, trace


def palindrome_npda(text):

    if any(char not in "01" for char in text):
        return False, ["Only binary digits 0 and 1 are allowed"]

    n = len(text)

    # Try all possible midpoint choices
    for midpoint in range(n + 1):

        # Even-length palindrome
        result, trace = simulate_branch(
            text, midpoint, False
        )

        if result:
            return True, trace

        # Odd-length palindrome
        if midpoint < n:

            result, trace = simulate_branch(
                text, midpoint, True
            )

            if result:
                return True, trace

    return False, ["No matching palindrome pattern found"]


def run_palindrome():

    print("\n===== PALINDROME CHECKER =====")
    print("Alphabet: 0 and 1")

    text = input("Enter binary string: ")

    result, trace = palindrome_npda(text)

    print("\nNPDA PROCESSING:")

    for step in trace:
        print(step)

    print("\nRESULT:", "ACCEPTED" if result else "REJECTED")


def test_palindrome():

    accepted = [
        "", "0", "1", "00", "11",
        "101", "1001", "0110", "01010"
    ]

    rejected = [
        "01", "10", "001", "110",
        "1011", "0100"
    ]

    print("\nPALINDROME TEST CASES")

    for item in accepted:
        result, _ = palindrome_npda(item)
        print(repr(item), ":", "Accepted" if result else "FAILED")

    for item in rejected:
        result, _ = palindrome_npda(item)
        print(repr(item), ":", "Rejected" if not result else "FAILED")