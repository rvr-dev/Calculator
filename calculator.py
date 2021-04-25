#
# Your previous Plain Text content is preserved below:
#
# Write a function/method that takes a mathematical expression represented as a
# string and returns the value of the expression.
#
# The expression is written in infix notation (number operator number).
# You only need to support four operations: addition, subtraction, division and multiplication.
# No parentheses and no operator precedence (simple left to right evaluation)
# You can't assume input will be valid but each term will be space-delimited.
#
# Example inputs:
# "15 + 2 - 3" => 14
# "1 + 232 / 233" => 1
# "2 * 3 + 12 / 6" => 3

from calculatoroperators import CalculatorOperators as Operators
from expression_dataclass import Expression


class Calculator:
    """Class to calculate string from left to right"""

    def __init__(self):
        pass

    @staticmethod
    def __count(expr: Expression) -> float:
        """controller for solving single-sign expressions with Calc_functions class"""
        return Operators.OPERATIONS[expr.sign](expr.result, expr.next_number)

    @staticmethod
    def __validate_float(number: str) -> float:
        """validates input numbers and signs"""
        # isdigit(), isnumeric() don't work with negative and fractional numbers
        num = number[1:] if number.startswith('-') else number
        num = num.replace('.', '', 1)
        # cut first '-' and one '.' to help isdigit cover all cases, another options try/except or regexp
        if num.isdigit():
            return float(number)
        else:
            raise ValueError(f'Wrong data. {number} is not a valid number')

    @staticmethod
    def __validate_sign(sign: str) -> str:
        if sign not in Operators.OPERATIONS:
            raise ValueError(f'{sign} is not an allowed sign')
        return sign

    def calculate(self, equation_string: str) -> float:
        """reads user input and solve expression using __count method"""
        equation = equation_string.split()
        expr = Expression()
        expr.result = None if not equation else Calculator.__validate_float(equation[0])
        for i in range(1, len(equation), 2):
            expr.sign = Calculator.__validate_sign(equation[i])
            expr.next_number = Calculator.__validate_float('' if i > len(equation) - 2 else equation[i + 1])
            expr.result = Calculator.__count(expr)
        return expr.result


if __name__ == '__main__':
    calc = Calculator()
    print(calc.calculate('3 + 11.2 * 5 / 2 - 11 + .5'))
