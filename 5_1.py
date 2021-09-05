with open('my_file5_1.txt', 'x') as f_obj:
    user_line = input('Введите текст: \n')
    while user_line:
        f_obj.write(f'{user_line}\n')
        user_line = input('Введите текст: \n')
