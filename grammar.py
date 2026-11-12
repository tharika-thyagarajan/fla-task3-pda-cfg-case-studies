"""
Formal Grammar Definitions for FLA Task 3
Case Studies:
1. Balanced Parentheses
2. Arithmetic Expressions
3. Binary Palindromes
"""

# ============================================================
# CASE STUDY 1: BALANCED PARENTHESES
# ============================================================

# Ambiguous Context-Free Grammar
BALANCED_AMBIGUOUS_CFG = {
    "S": [
        "SS",
        "(S)",
        "[S]",
        "{S}",
        "()",
        "[]",
        "{}"
    ]
}

# Revised Unambiguous Context-Free Grammar
BALANCED_REVISED_CFG = {
    "S": ["BS", "B"],
    "B": [
        "(S)",
        "()",
        "[S]",
        "[]",
        "{S}",
        "{}"
    ]
}


# ============================================================
# CASE STUDY 2: ARITHMETIC EXPRESSIONS
# ============================================================

# Ambiguous Grammar
ARITHMETIC_AMBIGUOUS_CFG = {
    "E": [
        "E+E",
        "E-E",
        "E*E",
        "E/E",
        "(E)",
        "id"
    ]
}

# Revised Grammar with Operator Precedence
ARITHMETIC_REVISED_CFG = {
    "E": ["E+T", "E-T", "T"],
    "T": ["T*F", "T/F", "F"],
    "F": ["(E)", "id"]
}

# Left-recursion-free Grammar for LL(1) Parsing
ARITHMETIC_LL1_CFG = {
    "E": ["TE'"],
    "E'": ["+TE'", "-TE'", "ε"],
    "T": ["FT'"],
    "T'": ["*FT'", "/FT'", "ε"],
    "F": ["(E)", "id"]
}


# ============================================================
# CASE STUDY 3: BINARY PALINDROMES
# ============================================================

# Grammar for binary palindromes
BINARY_PALINDROME_CFG = {
    "S": [
        "0S0",
        "1S1",
        "0",
        "1",
        "ε"
    ]
}

# Grammar for marked-centre binary palindromes
MARKED_PALINDROME_CFG = {
    "S": [
        "0S0",
        "1S1",
        "0",
        "1",
        "c",
        "ε"
    ]
}


# ============================================================
# GRAMMAR DISPLAY FUNCTION
# ============================================================

def display_grammar(title, grammar):
    print("\n" + "=" * 65)
    print(title)
    print("=" * 65)

    for non_terminal, productions in grammar.items():
        print(f"{non_terminal} -> {' | '.join(productions)}")


# ============================================================
# DISPLAY ALL GRAMMARS
# ============================================================

def display_all_grammars():

    display_grammar(
        "BALANCED PARENTHESES - AMBIGUOUS CFG",
        BALANCED_AMBIGUOUS_CFG
    )

    display_grammar(
        "BALANCED PARENTHESES - REVISED CFG",
        BALANCED_REVISED_CFG
    )

    display_grammar(
        "ARITHMETIC EXPRESSIONS - AMBIGUOUS CFG",
        ARITHMETIC_AMBIGUOUS_CFG
    )

    display_grammar(
        "ARITHMETIC EXPRESSIONS - PRECEDENCE CFG",
        ARITHMETIC_REVISED_CFG
    )

    display_grammar(
        "ARITHMETIC EXPRESSIONS - LL(1) CFG",
        ARITHMETIC_LL1_CFG
    )

    display_grammar(
        "BINARY PALINDROME CFG",
        BINARY_PALINDROME_CFG
    )

    display_grammar(
        "MARKED-CENTRE PALINDROME CFG",
        MARKED_PALINDROME_CFG
    )


if __name__ == "__main__":
    display_all_grammars()