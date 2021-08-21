month = input('Укажите порядковый номер месяца, пожалуйста: ')

wi = 'winter'
sp = 'spring'
su = 'summer'
au = 'autumn'

all_month = {'1': wi, '2': wi, '3': sp, '4': sp, '5': sp, '6': su, '7': su, '8': su, '9': au, '10': au, '11': au, '12': wi}

print(all_month[month]) #решение через словарь

season = (wi, wi, sp, sp, sp, su, su, su, au, au, au, wi)

print(season[int(month) - 1]) #решение через список
