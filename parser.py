import re


class ArithmeticExpressionParser:
    """
    Context-Free Grammar (CFG) parser
    for arithmetic expressions.

    Grammar:
    E  -> T E'
    E' -> + T E' | - T E' | epsilon
    T  -> F T'
    T' -> * F T' | / F T' | epsilon
    F  -> (E) | id | number
    """

    def __init__(self):
        self.tokens = []
        self.position = 0

    def tokenize(self, expression):
        pattern = r'\d+(?:\.\d+)?|[a-zA-Z_]\w*|[()+\-*/]'
        tokens = re.findall(pattern, expression)

        # Ensure no invalid characters are ignored.
        if ''.join(tokens) != re.sub(r'\s+', '', expression):
            raise ValueError("Invalid character")

        return tokens

    def current_token(self):
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return None

    def match(self, expected):
        if self.current_token() == expected:
            self.position += 1
            return True
        return False

    def parse_expression(self):
        self.parse_term()

        while self.current_token() in ('+', '-'):
            self.position += 1
            self.parse_term()

    def parse_term(self):
        self.parse_factor()

        while self.current_token() in ('*', '/'):
            self.position += 1
            self.parse_factor()

    def parse_factor(self):
        token = self.current_token()

        if token in ('+', '-'):
            self.position += 1
            self.parse_factor()

        elif token == '(':
            self.position += 1
            self.parse_expression()

            if not self.match(')'):
                raise ValueError("Missing closing parenthesis")

        elif token is not None and (
            re.fullmatch(r'\d+(?:\.\d+)?', token)
            or re.fullmatch(r'[a-zA-Z_]\w*', token)
        ):
            self.position += 1

        else:
            raise ValueError("Invalid expression")

    def validate(self, expression):
        try:
            self.tokens = self.tokenize(expression)
            self.position = 0

            if not self.tokens:
                return False

            self.parse_expression()

            return self.position == len(self.tokens)

        except (ValueError, TypeError):
            return False


if __name__ == "__main__":

    parser = ArithmeticExpressionParser()

    accepted = [
        "a+b",
        "2+3*4",
        "(5+2)*3",
        "a/b-c",
        "12*(x+3)",
        "-5+2"
    ]

    rejected = [
        "a+",
        "a**b",
        "(a+b",
        "a b",
        "5+*3",
        ""
    ]

    print("\nARITHMETIC EXPRESSION CFG PARSER")
    print("--------------------------------")

    print("\nACCEPTED TEST CASES")

    for expression in accepted:
        print(expression, ":",
              "Accepted" if parser.validate(expression) else "Rejected")

    print("\nREJECTED TEST CASES")

    for expression in rejected:
        print(expression, ":",
              "Rejected" if not parser.validate(expression) else "Accepted")