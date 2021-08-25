def my_func(num1, num2, num3):
    my_list = [num1, num2, num3]
    min_el = min(my_list)
    my_list.remove(min_el)
    return sum(my_list)

num1 = int(input('Введите число: '))
num2 = int(input('Введите еще одно число: '))
num3 = int(input('И третье число, пожалуйста, укажите: '))

print(my_func(num1, num2, num3))

