def count_even(number=11268):
    number = str(number)
    list_2 = [int(i) for i in number if int(i) % 2 == 0]
    # for i in list_1:
    #     if int(i) % 2 == 0:
    #         list_2.append(int(i))
    return sum(list_2)


print(count_even(123))
