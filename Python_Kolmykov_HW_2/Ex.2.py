def count_digit(string="test123;asjj32jdj"):
    list_1 = list(string)
    list_2 = [int(i) for i in list_1 if "0" <= i <= "9"]
    # for i in list_1:
    #     if "0" <= i <= "9":
    #         list_2.append(int(i))
    return sum(list_2)


print(count_digit())
