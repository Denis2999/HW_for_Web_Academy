import random

list_1 = []
for i in range(5):
    list_1.append(random.randint(-100, 100))

print("Изначальный список:", list_1)

list_2 = [x for x in list_1 if x % 2 != 0]  # Эту строку нашел в интернете, но не сильно понял
# Старался понять, но не понял, как работает эта строка
print("Список непарных чисел:", list_2)
