def is_growing(some_list=[10, 123, 500, 1000, 10001]):
    for i in range(1, len(some_list)):
        while some_list[i] < some_list[i + 1]:
            return True
        else:
            return False


print(is_growing([21, 412, 322, 42]))
