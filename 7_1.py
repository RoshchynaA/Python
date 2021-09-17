from random import randint

class Matrix:
    def __init__(self, numbers):
        self.numbers = numbers

    def __str__(self):
        s = ''
        for i in range(len(self.numbers)):
            for h in range(len(self.numbers[i])):
                s += f'{self.numbers[i][h]:02}'
            s += '\n'
        return s

    def __add__(self, other):
        numbers = [
            [self.numbers[i] [h] + other.numbers[i][h] for h in range(len(self.numbers[i]))]
                for i in range(len(self.numbers))]
        return Matrix(numbers)

first = Matrix([[randint(0, 10) for _ in range(10)] for _ in range(10)])
second = Matrix([[randint(0, 10) for _ in range(10)] for _ in range(10)])

print(first)
print(second)
print(first + second)


