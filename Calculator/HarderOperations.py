from Operation import IOperation


class Multiply(IOperation):

    def preform(self, num1, num2):
        return num1 * num2


class Divide(IOperation):

    def preform(self, num1, num2):
        return num1 / num2
