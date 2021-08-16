a = float(input('В первый день спортсмент пробежал: '))
b = float(input('Цель спортсмена: '))
day = 1
while a < b:
    a = a + a / 10
    day = day + 1
print(f'Нужное количество дней составит: {day}')