class SquareGenerator:
    def generate(self, start, end):
        if end < start:
            raise Exception("Exception: end value should be >= than start")
        return [i ** 2 for i in range(start, end + 1)]
