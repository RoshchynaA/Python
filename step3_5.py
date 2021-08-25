def my_func_sum (user_list):
    summ = 0
    for i in user_list:
        if i == 'stop':
            break
        else:
            summ = summ + int (i)

    return summ

stop = False
summ = 0
while not stop:
    user_list = input('Строка чисел, разделённых пробелом. Стоп-слово stop: ')
    my_list = user_list.split(' ')
    result = my_func_sum(my_list)
    summ = summ + result
    print(summ)

    if user_list.find('stop') != -1:
        stop = True

print(f'Итоговая сумма: {summ}')
