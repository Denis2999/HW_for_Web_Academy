def bubble_sort(some_list=[63, 80, 62, 69, 71, 37, 12, 90, 19, 67]):
    for i in range(len(some_list) - 1):
        for i in range(len(some_list) - i - 1):
            if some_list[i] > some_list[i + 1]:
                some_list[i], some_list[i + 1] = some_list[i + 1], some_list[i]
    return some_list


print(bubble_sort())
