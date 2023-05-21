from EasyOperations import Add, Subtract
from HarderOperations import Divide, Multiply


class Calculator:
    add_operation = Add()
    subtract_operation = Subtract()
    divide_operation = Divide()
    multiply_operation = Multiply()

    def add_numbers(self, num1, num2):
        return self.add_operation.preform(num1, num2)

    def extract_numbers(self, num1, num2):
        return self.subtract_operation.preform(num1, num2)

    def divide_numbers(self, num1, num2):
        return self.divide_operation.preform(num1, num2)

    def multiply_numbers(self, num1, num2):
        return self.multiply_operation.preform(num1, num2)
