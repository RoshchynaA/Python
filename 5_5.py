#почему не работает?
with open('my_file5_5.txt', 'w+') as file:
    summ = 0
    my_str = ('1 2 3 4 5)
    file.write(my_str)
    my_num = file.read().split()
    for num in my_num:
        summ += int(num)
print(summ)
