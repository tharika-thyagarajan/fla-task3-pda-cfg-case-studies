Case Study-Based Analysis and Design Using PDA and CFG

1. Project Overview

This project focuses on the implementation and analysis of three real-world language validation problems using Pushdown Automata (PDA) and Context-Free Grammars (CFG).

The project demonstrates how formal language concepts can be applied to recognize valid and invalid strings using stack-based processing, grammar rules, and automated testing.

Course: Formal Language and Automata Theory (FLA)
Task: Assessment Task 3
Programming Language: Python

2. Objectives

- To understand the practical applications of PDA and CFG.
- To design a PDA for balanced parentheses validation.
- To develop a CFG-based arithmetic expression validator.
- To implement a Non-Deterministic Pushdown Automaton (NPDA) for binary palindrome recognition.
- To validate accepted and rejected input strings.
- To perform automated testing and analyze the results.

3. Case Studies Implemented

Case Study 1: Balanced Parentheses Checker Using PDA

Objective: To verify whether an expression contains correctly matched and properly nested parentheses.

Concept Used: Pushdown Automaton (PDA).

Working Principle:

- The PDA uses a stack to track opening parentheses.
- When an opening parenthesis is encountered, it is pushed onto the stack.
- When a closing parenthesis is encountered, the corresponding opening parenthesis is popped.
- If a mismatch occurs or the stack is not empty at the end, the string is rejected.
- Otherwise, the string is accepted.

Sample Test Cases:

Input| Result
"()"| Accepted
"(())"| Accepted
"(()())"| Accepted
"("| Rejected
"())"| Rejected

Case Study 2: Arithmetic Expression Validator Using CFG

Objective: To validate arithmetic expressions based on grammatical rules.

Concept Used: Context-Free Grammar (CFG).

Grammar Productions:

E → T E'
E' → + T E' | - T E' | ε
T → F T'
T' → * F T' | / F T' | ε
F → (E) | number

Working Principle:

- The grammar defines the valid structure of arithmetic expressions.
- The parser checks whether the input follows the grammar productions.
- It validates operands, operators, and parentheses.
- Expressions that follow the grammar are accepted; invalid expressions are rejected.

Sample Test Cases:

Input| Result
"a+b*c"| Accepted
"(a+b)*c"| Accepted
"12*(x+3)"| Accepted
"a+b*"| Rejected
"a b"| Rejected

Case Study 3: Binary Palindrome Checker Using NPDA

Objective: To identify whether a binary string reads the same forward and backward.

Concept Used: Non-Deterministic Pushdown Automaton (NPDA).

Working Principle:

- The NPDA reads the binary input string.
- It pushes the first portion of the input onto the stack.
- It nondeterministically guesses the midpoint of the string.
- For odd-length strings, the middle symbol is skipped.
- It compares the remaining input with the symbols stored in the stack.
- If all symbols match and the stack becomes empty, the string is accepted.

Sample Test Cases:

Input| Result
"0"| Accepted
"1"| Accepted
"00"| Accepted
"101"| Accepted
"1001"| Accepted
"011"| Rejected
"0100"| Rejected

4. Technologies Used

- Python 3
- PyCharm IDE
- Pushdown Automata (PDA)
- Non-Deterministic Pushdown Automata (NPDA)
- Context-Free Grammar (CFG)
- Stack Data Structure
- Automated Testing

5. Project Structure

fla_task3/
│
├── diagrams/
│   ├── 01_balanced_parentheses_pda.svg
│   ├── 02_arithmetic_expression_cfg.svg
│   └── 03_binary_palindrome_npda.svg
│
├── pda_cfg/
│   ├── __init__.py
│   ├── grammar.py
│   ├── parser.py
│   └── pda.py
│
├── screenshots/
│
├── tests/
│   ├── test_arithmetic.py
│   ├── test_balanced.py
│   └── test_palindrome.py
│
├── tools/
│   ├── automated_testing.py
│   └── make_diagrams.py
│
├── arithmetic_expression.py
├── balanced_parentheses.py
├── main.py
├── palindrome_checker.py
├── README.md
└── requirements.txt

6. Execution Instructions

1. Install Python 3 on your system.
2. Open the project folder in PyCharm.
3. Open "main.py".
4. Run the program.
5. Select the required case study from the menu.
6. Enter an input string to check whether it is accepted or rejected.

To execute automated testing, run:

python tools/automated_testing.py

To generate the diagrams, run:

python tools/make_diagrams.py

7. Automated Testing and Results

Automated testing was performed to verify the correctness of the three case studies.

Final Testing Results:

Evaluation| Result
Total Test Cases| 15
Passed| 15
Failed| 0
Success Rate| 100%

All 15 automated test cases passed successfully.

The testing process confirms that the implemented validators correctly identify the expected accepted and rejected input strings in the selected test cases.

8. Advantages

- Demonstrates practical applications of formal language theory.
- Provides clear separation between different validation problems.
- Uses stack-based processing for nested and palindrome structures.
- Supports automated testing.
- Helps understand the differences between PDA, NPDA, and CFG.

9. Conclusion

This project successfully demonstrates three applications of formal languages using Pushdown Automata, Non-Deterministic Pushdown Automata, and Context-Free Grammars.

The balanced parentheses checker validates nested structures, the arithmetic expression validator checks grammatical correctness, and the binary palindrome checker recognizes symmetrical binary strings.

The implementation achieved 15 successful test cases out of 15, demonstrating the expected functionality of the implemented validators.

10. Future Enhancements

- Develop a graphical user interface for input validation.
- Extend the arithmetic grammar to support additional operators.
- Improve error reporting for invalid expressions.
- Support more complex formal language recognition problems.
- Expand automated testing with additional edge cases.

11. References

1. Introduction to Automata Theory, Languages, and Computation – John E. Hopcroft, Rajeev Motwani, and Jeffrey D. Ullman.
2. Formal Languages and Automata Theory course materials.
3. Python Official Documentation – https://docs.python.org/3/
4. Context-Free Grammars and Pushdown Automata – Course reference materials.