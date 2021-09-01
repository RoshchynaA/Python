first_list = [28, 55, 2, 8, 13, 4, 39, 7, 45]
result_list = [first_list [i] for i in range(1, len(first_list)) if first_list[i] > first_list [i -1]]
print(result_list)
