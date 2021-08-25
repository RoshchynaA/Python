def func_str():
    str = ('Меня зовут ' + name + ' ' + surname + ', ' + year + ' года рождения. Проживаю в городе ' + town + '. Связаться со мной можно по емейлу ' + email + ' или по телефону ' + phone)
    return str

name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year = input('Введите год рождения: ')
town = input('Введите город проживания: ')
email = input('Введите электронный почтовый адрес: ')
phone = input('Введите телефон: ')

print(func_str())
