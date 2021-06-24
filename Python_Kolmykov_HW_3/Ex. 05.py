def season(quart=2):
    if 1 <= quart <= 2 or quart == 12:
        return "Зима"
    elif 3 <= quart <= 5:
        return "Весна"
    elif 6 <= quart <= 8:
        return "Лето"
    elif 9 <= quart <= 11:
        return "Осень"


month = int(input("Введи номер номер месяца: "))
print(season(month))
