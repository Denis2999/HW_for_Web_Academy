def two_lists(list_1, list_2):
    d1 = {}
    for i1, i2 in zip(list_1, list_2):
        d1[i1] = i2
    return d1


l_1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
l_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(two_lists(l_1, l_2))
