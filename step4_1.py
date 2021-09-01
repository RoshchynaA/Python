import sys
from sys import argv

if len(sys.argv) < 4:
    raise ValueError('Введите все необходимые данные, пожалуйста (выработка в часах, ставка в час, премия)')
else:
    production = float(sys.argv[1])
    bet = float(sys.argv[2])
    prize = float(sys.argv[3])
    salary = production * bet + prize
    print(salary)
