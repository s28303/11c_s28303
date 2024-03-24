from abc import ABC, abstractmethod


class AbstractSquareGenerator(ABC):
    @abstractmethod
    def generate_squares(self, start, end):
        pass


class SquareGenerator(AbstractSquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            raise Exception("Exception: end value should be >= than start")
        return [i ** 2 for i in range(start, end + 1)]
