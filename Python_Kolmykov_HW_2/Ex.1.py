def join_str(string="lorem ipsum A string some text", N=5):
    list_1 = string.split(" ")
    list_2 = [i for i in list_1 if len(i) >= N]
    # list_2 = []
    # for i in list_1:
    #     if len(i) >= N:
    #         list_2.append(i)
    return list_2


print(join_str())
