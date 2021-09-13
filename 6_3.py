class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return "{0} {1}".format(self.name, self.surname)

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


workman = Position('Liza', 'Ivanova', 'doctor', 700, 130)
print(workman.name)
print(workman.surname)
print(workman.position)
print(workman._income)
print(workman.get_full_name())
print(workman.get_total_income())
