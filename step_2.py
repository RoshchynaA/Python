time = int(input("Enter time in second, please:"))
h = time // 3600
m = time % 3600
mn = m // 60
sec = m % 60

a_formated = f"It's {h} hour {mn} minute {sec} second"
print(a_formated)
