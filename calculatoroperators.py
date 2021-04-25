class CalculatorOperators:
    """operator functions for Calculator class"""
    def __init__(self):
        pass

    @staticmethod
    def calc_add(*args):
        """adds 2 numbers"""
        return args[0] + args[1]

    @staticmethod
    def calc_subtract(*args):
        """subtracts 2 numbers"""
        return args[0] - args[1]

    @staticmethod
    def calc_multiply(*args):
        """multiplies 2 numbers"""
        return args[0] * args[1]

    @staticmethod
    def calc_divide(*args):
        """divides 2 numbers"""
        if args[1] != 0:
            return args[0] / args[1]
        else:
            raise ZeroDivisionError

    OPERATIONS = {
        '+': calc_add.__func__,
        '-': calc_subtract.__func__,
        '*': calc_multiply.__func__,
        '/': calc_divide.__func__
    }
