def print_odd_index(some_list=[14, 56, 23, 22, 7, 8, 4, 34, 45, 3]):
    for i in range(len(some_list)):
        if i % 2 != 0:
            print(some_list[i])


print(print_odd_index())
