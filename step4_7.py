def generator(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
        yield x

n = 10

for el in generator(n):
    print(f'{el}')

# чтобы пронумеровать
# for ind, el in enumerate(generator(n)):
#     print(f'№{ind +1} {el}')