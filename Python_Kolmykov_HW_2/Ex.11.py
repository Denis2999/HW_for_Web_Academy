def most_common(some_list=[1, 1, 1, 2, 3, 4, 123, 123, 123, 123, 5, 2]):
    most_common_1 = None
    most_common_2 = 0

    for i in set(some_list):
        qty = some_list.count(i)
        if qty > most_common_2:
            most_common_2 = qty
            most_common_1 = i
    return most_common_1


print(most_common())
