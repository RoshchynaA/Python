with open('my_file5_2.txt') as file:
    content = file.readlines()
    for num, line in enumerate(content):
        content_word = len(line.split())
        print(f'В строке №{num + 1} определено {content_word} слов')
