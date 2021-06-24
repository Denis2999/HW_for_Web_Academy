def calc_many_numbers(n, m):
    counter = 0
    for i in range(1, m + 1):
        num = int(str(n) * i)
        counter += num
        if i != m:
            print(num, end=" + ")
        else:
            print(num, end=" = ")
    return counter


print(calc_many_numbers(7, 4))
