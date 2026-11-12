class PushdownAutomaton:

    def balanced_parentheses(self, expression):
        stack = []

        matching = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in expression:
            if char in "([{":
                stack.append(char)

            elif char in ")]}":
                if not stack or stack[-1] != matching[char]:
                    return False

                stack.pop()

        return len(stack) == 0

    def binary_palindrome(self, string):

        if any(char not in "01" for char in string):
            return False

        # NPDA: Guess the midpoint.
        # Test both even and odd length palindromes.

        for midpoint in range(len(string) + 1):

            # Even-length palindrome
            first_half = string[:midpoint]
            second_half = string[midpoint:]

            if first_half == second_half[::-1]:
                return True

            # Odd-length palindrome:
            # Skip the middle symbol.
            if midpoint < len(string):

                first_half = string[:midpoint]
                second_half = string[midpoint + 1:]

                if first_half == second_half[::-1]:
                    return True

        return False

    def arithmetic_expression(self, expression):
        import ast

        try:
            tree = ast.parse(expression, mode="eval")

            allowed_nodes = (
                ast.Expression, ast.BinOp, ast.UnaryOp,
                ast.Constant, ast.Add, ast.Sub, ast.Mult,
                ast.Div, ast.FloorDiv, ast.Mod, ast.Pow,
                ast.UAdd, ast.USub, ast.Load
            )

            for node in ast.walk(tree):
                if not isinstance(node, allowed_nodes):
                    return False

                if isinstance(node, ast.Constant):
                    if not isinstance(node.value, (int, float)):
                        return False

            return True

        except (SyntaxError, ValueError, TypeError):
            return False