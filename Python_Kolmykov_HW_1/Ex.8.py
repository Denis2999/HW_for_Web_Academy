A = int(input("Введи первое число: "))
B = int(input("Введи второе число: "))
list_1 = []

if A < B:
    for i in range(A, B):
        list_1.append(i)
else:
    for i in range(B, A):
        list_1.append(i)
    list_1.reverse()
print("Готовый список:", list_1)
