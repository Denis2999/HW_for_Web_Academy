def math_block(m, a, b):
    for i in range(a, b + 1):
        print("{}x{}={}".format(m, i, m * i))


m_1 = int(input("Enter first number: "))
a_1 = int(input("Enter second number: "))
b_1 = int(input("Enter third number: "))
print(math_block(m_1, a_1, b_1))
