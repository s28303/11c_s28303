import math

from square_generator_package import SquareGenerator

squares = [i ** 2 for i in range(1, 11)]
print(squares)


def generate_squares(start, end):
    return [i ** 2 for i in range(start, end + 1)]


print(generate_squares(1, 10))

sg = SquareGenerator()
sg_squares = sg.generate(1, 10)
print(sg_squares)

roots = [math.sqrt(i) for i in sg_squares]
print(roots)

try:
    sg_squares_exception = sg.generate(10, 1)
except Exception as e:
    print(e)
