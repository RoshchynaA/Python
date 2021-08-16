plus = int(input('Укажите выручку'))
minus = int(input('Укажите издержки'))

if minus > plus:
    print('Работаете в убыток')
elif plus > minus:
    print('Работаете в плюс')
    rent = (plus - minus) / plus
    print(f'Рентабельность составила: {rent}')

    people = int(input('Введите число сотрудников: '))
    people_plus = (plus - minus) / people
    print(f'Прибыль каждого сотрудника: {people_plus}')
elif plus == minus:
    print('Нулевая прибыль')

