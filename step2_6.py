product = []
count = 1
instruction = ''

while instruction != 'stop':
    title = input('Название товара: ')
    cost = input('Стоимость товара: ')
    quantity = input('Количество товара: ')
    unit = input('Единица измерения товара: ')
    product.append(
        (count, {'title': title, 'cost': cost, 'quantity': quantity, 'unit': unit})
    )
    count += 1
    instruction = input('Напишите "stop", если указали все необходимые данные')

prod_list = {}

for num, product_dict in product:
    for key, value in product_dict.items():
        if not prod_list.get(key):
            prod_list[key] = [value]
        else:
            prod_list[key].append(value)

for key, value in prod_list.items():
        prod_list[key] = list(set(value))

print(prod_list)

