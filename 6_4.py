class Car:
    def __init__(self, speed, colour, name, is_police = False):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Go!")

    def stop(self):
        print('STOP')

    def turn(self, direction):
        print(f"Car turned to {direction}")

    def show_speed(self):
        print(f'Your speed now {self.speed}')

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Your speed is exceeded!")


class PoliceCar(Car):
    def __init__(self, speed, colour, name):
        super().__init__(speed, colour, name, True)


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Your speed is exceeded!")

class SportCar(Car):
    pass

mytowncar = TownCar(60, 'white', 'Audi')
myworkcar = WorkCar(50, 'black', 'Toyota')
mysportcar = SportCar(100, 'red', 'Ferrari')
mypolisecar = PoliceCar(20, 'blue', 'Oka')

mytowncar.show_speed()
myworkcar.show_speed()

myworkcar.speed = 10
myworkcar.show_speed()

mypolisecar.turn('back')
