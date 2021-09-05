my_nums = {"One": 'Один', "Two": 'Два', "Three": 'Три', "Four": 'Четыре'}

with open('my_file5_4.txt') as file, open('new_my_file5_4.txt', 'w') as new_file:
    content = file.readlines()
    for line in content:
        data = line.split()
        ru_nums = my_nums.get(data[0])
        new_file.write(f'{line.replace(data[0], ru_nums)}')
