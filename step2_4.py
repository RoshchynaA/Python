list = input('Введите несколько слов: ')
spl_list = list.split()

for num, word in enumerate(spl_list):
    print(f'{num + 1} - {word[:10]}')


