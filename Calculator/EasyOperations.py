from Operation import IOperation


class Add(IOperation):

    def preform(self, num1, num2):
        return num1 + num2


class Subtract(IOperation):

    def preform(self, num1, num2):
        return num1 - num2
