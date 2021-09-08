class Stationery:
    def __init__(self, title):

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        super().draw()
        print('Запуск отрисовки ручкой')

class Pencil(Stationery):
    def draw(self):
        super().draw()
        print('Запуск отрисовки карандашом')

class Handle(Stationery):
    def draw(self):
        super().draw()
        print('Запуск отрисовки маркером')


mypen = Pen
mypencil = Pencil
myhandle = Handle

mypen.draw()
mypencil.draw()
myhandle.draw()