def int_func(a):
    word = a[0].upper() + a[1:].lower()
    return word

user_word = input('Введите слово из маленьких латинских букв: ')

print(f'{int_func(user_word)} ')

#вторая часть задания
user_string = input('Введите строку из латинских букв, разделенную пробелами: ')
for i in user_string.split(' '):
    print(f'{int_func(i)} ', end= '')
