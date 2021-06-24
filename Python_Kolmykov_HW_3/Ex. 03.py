numbers = input("Введи последовательность чисел: ")
list_1 = numbers.split(",")
print(type(list_1), "это список", list_1)
print(type(tuple(list_1)), "это кортеж", tuple(list_1))
