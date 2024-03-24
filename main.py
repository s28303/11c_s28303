squares = [i**2 for i in range(1, 11)]
print(squares)


def generate_squares(start, end):
    return [i**2 for i in range(start, end+1)]


print(generate_squares(1, 10))