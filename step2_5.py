list = [8, 8, 7, 6, 5, 3, 3, 2]
user_number = int(input('Введите целое число: '))

inserted = False

for index, elem in enumerate (list):
    if user_number > elem:
        list.insert(index, user_number)
        inserted = True
        break

if not inserted:
    list.append(user_number)

print(list)
