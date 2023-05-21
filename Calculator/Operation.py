from abc import ABC, abstractmethod


class IOperation(ABC):

    @abstractmethod
    def preform(self, num1, num2):
        pass
