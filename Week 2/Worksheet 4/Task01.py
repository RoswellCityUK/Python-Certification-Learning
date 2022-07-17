import enum


class Operator(enum.Enum):
    PLUS = '+'
    MINUS = '-'
    MULTIPLY = '*'
    DIVIDE = '/'


class Calculator:
    def __init__(self, operator: Operator, number_1: float, number_2: float):
        self.__operator = operator
        self.number_1 = number_1
        self.number_2 = number_2
        print(self.number_1, self.__operator.value, self.number_2)

    def __init__(self, operator: str, number_1: float, number_2: float):
        self.__operator = Operator(operator)
        self.number_1 = number_1
        self.number_2 = number_2

    def get_operator(self):
        return self.__operator.value

    def set_operator(self, operator: Operator):
        self.__operator = operator

    def set_operator(self, operator: str):
        self.__operator = Operator(operator)

    def get_num1(self):
        return self.number_1

    def get_num2(self):
        return self.number_2

    def get_result(self):
        if self.__operator == Operator.PLUS:
            return self.number_1 + self.number_2
        elif self.__operator == Operator.MINUS:
            return self.number_1 - self.number_2
        elif self.__operator == Operator.MULTIPLY:
            return self.number_1 * self.number_2
        elif self.__operator == Operator.DIVIDE:
            return self.number_1 / self.number_2
        else:
            raise ArithmeticError


x = Calculator('*', 6, 3)
print(x.get_num1(), x.get_operator(), x.get_num2(), "=", x.get_result())


x = Calculator(Operator.MINUS, 10, 5)
print(x.get_num1(), x.get_operator(), x.get_num2(), "=", x.get_result())


x = Calculator('+', 5, 12.4)
print(x.get_num1(), x.get_operator(), x.get_num2(), "=", x.get_result())


x = Calculator(Operator.DIVIDE, 2, 6)
print(x.get_num1(), x.get_operator(), x.get_num2(), "=", x.get_result())
