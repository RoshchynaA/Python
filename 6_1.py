from time import sleep

class TrafficLight:
    colours = ('red', 'yellow', 'green')
    period = (7, 2, 8)

    def __init__(self, colour):
        self.__colour = colour
        color = 'red'

    def running(self):
        while True:
            for i in self.colours:
                self.__colour = i
                print(self.__colour)
                sleep(self.period[self.colours.index(self.__colour)])


out_traffic_light = TrafficLight('red')
out_traffic_light.running()

