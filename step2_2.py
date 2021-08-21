your_list = input('Составьте список, пожалуйста: ')
sep_list = your_list.split( )

for i in range(len(sep_list) // 2):
    m1, m2 = 2 * i, 2 * i +1
    sep_list[m1], sep_list[m2] = sep_list[m2], sep_list[m1]

print(sep_list)
