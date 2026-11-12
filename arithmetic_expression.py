# FLA TASK 3 - CASE STUDY 2
# ARITHMETIC EXPRESSION VALIDATOR USING CFG AND PDA

import re


def tokenize(expression):

    tokens = []
    position = 0

    pattern = r"\d+|[A-Za-z][A-Za-z0-9]*|[()+\-*/]"

    while position < len(expression):

        if expression[position].isspace():
            position += 1
            continue

        match = re.match(pattern, expression[position:])

        if not match:
            return None

        value = match.group()

        if value.isdigit():
            tokens.append("NUM")
        elif value[0].isalpha():
            tokens.append("ID")
        else:
            tokens.append(value)

        position += len(value)

    tokens.append("$")
    return tokens


def arithmetic_pda(expression):

    tokens = tokenize(expression)

    if tokens is None:
        return False, ["Invalid character"]

    grammar = {
        "E": {
            "ID": ["T", "E'"],
            "NUM": ["T", "E'"],
            "(": ["T", "E'"]
        },

        "E'": {
            "+": ["+", "T", "E'"],
            "-": ["-", "T", "E'"],
            ")": [],
            "$": []
        },

        "T": {
            "ID": ["F", "T'"],
            "NUM": ["F", "T'"],
            "(": ["F", "T'"]
        },

        "T'": {
            "*": ["*", "F", "T'"],
            "/": ["/", "F", "T'"],
            "+": [],
            "-": [],
            ")": [],
            "$": []
        },

        "F": {
            "(": ["(", "E", ")"],
            "ID": ["ID"],
            "NUM": ["NUM"]
        }
    }

    terminals = {
        "ID", "NUM", "+", "-", "*", "/", "(", ")", "$"
    }

    stack = ["$", "E"]
    index = 0
    trace = []

    while stack:

        top = stack.pop()
        lookahead = tokens[index]

        if top in terminals:

            if top == lookahead:

                trace.append("Matched: " + top)

                if top == "$":
                    return True, trace

                index += 1

            else:
                trace.append(
                    "Expected " + top + ", found " + lookahead
                )
                return False, trace

        else:

            production = grammar.get(top, {}).get(lookahead)

            if production is None:
                trace.append(
                    "No valid production for " + top
                )
                return False, trace

            if production:
                stack.extend(reversed(production))
                trace.append(
                    top + " -> " + " ".join(production)
                )
            else:
                trace.append(top + " -> epsilon")

    return False, trace


def run_arithmetic():

    print("\n===== ARITHMETIC EXPRESSION VALIDATOR =====")
    print("Operators: +, -, *, /")
    print("Supports numbers, variables and parentheses.")

    expression = input("Enter expression: ")

    result, trace = arithmetic_pda(expression)

    print("\nPARSING TRACE:")

    for step in trace:
        print(step)

    print("\nRESULT:", "ACCEPTED" if result else "REJECTED")


def test_arithmetic():

    accepted = [
        "a+b*c",
        "(a+b)*c",
        "12*(x+3)",
        "a/b-c",
        "42"
    ]

    rejected = [
        "a+*b",
        "(a+b",
        "a b",
        "*a",
        "a+"
    ]

    print("\nARITHMETIC EXPRESSION TEST CASES")

    for item in accepted:
        result, _ = arithmetic_pda(item)
        print(item, ":", "Accepted" if result else "FAILED")

    for item in rejected:
        result, _ = arithmetic_pda(item)
        print(item, ":", "Rejected" if not result else "FAILED")