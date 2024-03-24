from square_generator_package import AbstractSquareGenerator


class CubicGenerator(AbstractSquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            raise Exception("Exception: end value should be >= than start")
        return [i ** 3 for i in range(start, end + 1)]
