def validate_password(password1="Password123P!", password2="Password123P!"):
    if password1 == password2:
        if len(password1) >= 8:
            list_1 = list(password1)
            counter = 0
            for i in list_1:
                if 65 <= ord(i) <= 90:
                    counter += 1
            if counter >= 2:
                if "!" or "?" or ";" or ":" or "%" or "*" in list_1:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


print(validate_password())
