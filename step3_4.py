def my_func(x,y):
    result = x ** y
    return result

x = int(input('Введите положительное число: '))
y = int(input('Введите целое отрицательное число: '))

print(my_func(x, y))
#вариант решения через звёздочки

def my_func(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
        return 1 / result

x = float(input('Введите положительное число: '))
y = int(input('Введите целое отрицательное число: '))

print(my_func(x, y))

#вариант решения через цикл