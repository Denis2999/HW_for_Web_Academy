list_1 = [1324, 543, -43, -56, 0, 664, 56, -546]
for i in range(len(list_1)):
    if list_1[i] < 0:
        list_1[i] = -1
    elif list_1[i] > 0:
        list_1[i] = 1

print(list_1)
