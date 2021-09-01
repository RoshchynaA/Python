from itertools import count, cycle

for el in count (2):
    if el > 12:
        break
    else:
        print(el)

x = 0
for el in cycle ('pur'):
    if x > 8:
        break
    print(el)
    x += 1
