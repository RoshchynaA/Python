def my_func_del (num1, num2):
    try:
        result_del = num1 / num2
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
        result_del = 0
    return result_del

num1 = int(input('Введите число: '))
num2 = int(input('Теперь введите еще одно число: '))

print(my_func_del(num1, num2))
