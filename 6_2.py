class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width


    def massa_asfalta(self, massa_asf_odin, thickness):
        return self._length * self._width * massa_asf_odin * thickness / 1000

my_road = Road(200, 66)
print(my_road.massa_asfalta(40, 4))
