def dict_sum(dict1):
    multip = 1
    for i in dict1:
        multip *= dict1[i]
    return multip


d1 = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
}
print(dict_sum(d1))
