x1 = float(input("Введи координаты x1: "))
y1 = float(input("Введи координаты y1: "))
x2 = float(input("Введи координаты x2: "))
y2 = float(input("Введи координаты y2: "))

A = x2 - x1
B = y2 - y1

length = (A ** 2 + B ** 2) ** (1 / 2)

print("Длина вектора равна", length)
