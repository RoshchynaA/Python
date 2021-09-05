#не понимаю, что в этом решении не так
with open('my_file5_3.txt') as file:
    content = file.readlines()
    summa = 0
    staff = {}
    for line in content:
        one_of_staff = line.split()
        staff.update({one_of_staff[0]: float(one_of_staff[1])})
        summa += float(one_of_staff[1])
aver_sal = summa / len(staff)
print(f'Средняя зарплата у сотрудников предприятия составляет {aver_sal}')

for one_of_staff[0], one_of_staff[1] in staff:
     if one_of_staff[1] < 20000:
        print(f'Оклад меньше 20000 у сотрудника {one_of_staff[0]}')

