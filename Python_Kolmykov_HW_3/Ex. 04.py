list_1 = [1, 2, 3]
list_2 = [11, 22, 33]
for i in range(len(list_1)):
    list_2.insert(i * 2, list_1[i])
print(list_2)
