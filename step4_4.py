first_list = [5, 5, 13, 22, 9, 65, 13, 6, 49, 11, 22, 9, 5, 11, 49, 734]
result_list = [i for i in first_list if first_list.count(i) == 1]
print(result_list)