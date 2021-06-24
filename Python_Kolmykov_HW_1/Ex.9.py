# n = int(input("Введи длину ромба: "))
# k = n // 2
# for i in range(k + 1):
#     if i == 0:
#         print(" " * (k - i), '*', sep='', end='\n')
#     else:
#         j = list(range(1, n - 1, 2))[i - 1]
#         print(" " * (k - i), '*', " " * j, '*', sep='', end='\n')
# for i in range(k - 1, -1, -1):
#     if i > 0:
#         j = list(range(n - k + (n - 9) // 2, -1, -2))[k - i - 1]
#         print(" " * (k - i), '*', " " * j, '*', sep='', end='\n')
#     else:
#         print(" " * (k - i), '*', sep='', end='\n')

for i in range(5):
    print(" " * (5 - i), "*" * i, end="")
    print("*" * (i - 1))

for i in range(5, 0, -1):
    print(" " * (5 - i), "*" * i, end="")
    print("*" * (i - 1))
