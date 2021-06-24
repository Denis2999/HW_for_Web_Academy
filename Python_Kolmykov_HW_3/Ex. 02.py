def get_ext(name='text.txt'):
    import os

    extension = os.path.splitext(name)[1][1:]
    if extension != "":
        return extension
    else:
        raise ValueError("!!!!!")


print(get_ext("somefile.txt.log"))
