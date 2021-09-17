from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def cost(self):
        pass

class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def cost(self):
        return self.v / 6.5 + 0.5

class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def cost(self):
        return self.h * 2 + 0.3

my_coat = Coat(45)
my_suit = Suit(33)
print(my_coat.cost)
print(my_suit.cost)
