num = int(input('Enter integer positive number'))
a_num = 0
while num > 0:
    if num % 10 > a_num:
        a_num = num % 10
        if a_num == 9:
            break
    num = num // 10

print(f'The largest digit of the number: {a_num} ')