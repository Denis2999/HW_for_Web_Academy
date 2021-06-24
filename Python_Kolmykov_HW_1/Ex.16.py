year = int(input("Введите год: "))
if year % 400 == 0:
    print("Это високосный год")
elif year % 100 == 0 & year % 4 == 0:
    if year % 100 == 0:
        print("Это обычный год")
    else:
        print("Это високосный год")
elif year % 4 == 0:
    print("Это високосный год")
else:
    print("Это обычный год")
