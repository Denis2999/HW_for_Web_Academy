def compare_sequence(list_1, list_2):
    counter = 0
    for i in list_1:
        if i in list_2:
            counter += 1
    if counter > 0:
        return True
    else:
        return False


print(compare_sequence([1, 2, 3, 434, 53], [1, 3]))
