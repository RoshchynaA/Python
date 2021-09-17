class Cell:
    def __init__(self, piece):
        self.piece = piece

    def __add__(self, other):
        return Cell(self.piece + other.piece)

    def __sub__(self, other):
        res = self.piece - other.piece
        if res >= 0:
            return Cell(res)
        else:
            print(f"Error")

    def __mul__(self, other):
        return Cell(self.piece * other.piece)

    def __truediv__(self, other):
        return Cell(self.piece // other.piece)

    def make_order(self, count):
        a = ""
        for i in range(self.piece // count):
            a += '*' * count + '\n'
        a += '*' * (self.piece % count) + '\n'
        return a

    def __str__(self):
        return f'{self.piece}'


my_cell = Cell(9)
print(my_cell.make_order(11))

my_cell2 = Cell(13)
print(my_cell2.make_order(10))

print(my_cell + my_cell2)
print(my_cell - my_cell2)
print(my_cell2 - my_cell)
print(my_cell * my_cell2)
print(my_cell / my_cell2)



