import json

firms = {}
plus_sum = 0
plus_count = 0

with open('my_file5_7.txt') as file:
    file_lines = file.readlines()
    for line in file_lines:
        money = line.split()
        profit = float(money[2]) - float(money[3])
        firms.update({money[0]: profit})
        if profit > 0:
            plus_count += 1
            plus_sum += profit

av_profit = plus_sum / plus_count
result = [firms, {'Average profit': av_profit}]

with open('result.json', 'w') as file:
    json.dump(result, file)
