num_1 = int(input("Введи первое число: "))
num_2 = int(input("Введи второе число: "))

if num_1 % num_2 == 0:
    print("Числа делятся без остатка")
else:
    print("Остаток равен", num_1 % num_2)

print("Частное равно", int(num_1 / num_2))