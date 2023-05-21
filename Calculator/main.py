from Calculator import *


if __name__ == '__main__':
    my_calculator = Calculator()

    print(my_calculator.add_numbers(1, 2))
    print(my_calculator.add_numbers(my_calculator.multiply_numbers(3, 5), 2))
