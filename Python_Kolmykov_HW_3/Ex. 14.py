import requests

exchange_list = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5").json()
print("            ***** Currency Exchange *****")
for i in exchange_list:
    print(i)

print()
type_operation = input("Choose type of your operation (sale or buy)   >>> ")
type_operation = type_operation.lower()

if type_operation == "sale":
    curr = input("Which currency would you sell?   >>> ")
    curr = curr.upper()
    price = int(input("How much?   >>> "))

    if curr == "USD":
        buy_curr = input("Which currency would you buy? >>>")
        buy_curr = buy_curr.upper()
        if buy_curr == "UAH":
            print("You'll get: ", price * float(exchange_list[0]["buy"]))
        elif buy_curr == "BTC":
            print("You'll get: ", price * float(exchange_list[3]["buy"]))
        else:
            print("Unfortunately, this is not possible")
    elif curr == "EUR":
        buy_curr = input("Which currency would you buy? >>>")
        buy_curr = buy_curr.upper()
        if buy_curr == "UAH":
            print("You'll get: ", price * float(exchange_list[1]["buy"]))
        else:
            print("Unfortunately, this is not possible")
    elif curr == "RUR":
        buy_curr = input("Which currency would you buy? >>>")
        buy_curr = buy_curr.upper()
        if buy_curr == "UAH":
            print("You'll get: ", price * float(exchange_list[2]["buy"]))
        else:
            print("Unfortunately, this is not possible")
    elif curr == "BTC":
        buy_curr = input("Which currency would you buy? >>>")
        buy_curr = buy_curr.upper()
        if buy_curr == "USD":
            print("You'll get: ", price * float(exchange_list[3]["buy"]))
        else:
            print("Unfortunately, this is not possible")
    elif curr == "UAH":
        buy_curr = input("Which currency would you buy? >>>")
        buy_curr = buy_curr.upper()
        if buy_curr == "USD":
            print("You'll get: ", price * float(exchange_list[0]["buy"]))
        elif buy_curr == "EUR":
            print("You'll get: ", price * float(exchange_list[1]["buy"]))
        elif buy_curr == "RUR":
            print("You'll get: ", price * float(exchange_list[2]["buy"]))
        else:
            print("Unfortunately, this is not possible")
    else:
        print("Undefined currency")
elif type_operation == "buy":
    curr = input("Which currency would you sell?   >>> ")
    curr = curr.upper()
    price = input("How much?   >>> ")

    if curr == "USD":
        buy_curr = input("Which currency would you sell? >>>")
        buy_curr = buy_curr.upper()
        if buy_curr == "UAH":
            print("You'll get: ", price * float(exchange_list[0]["sale"]))
        elif buy_curr == "BTC":
            print("You'll get: ", price * float(exchange_list[3]["sale"]))
        else:
            print("Unfortunately, this is not possible")
    elif curr == "EUR":
        buy_curr = input("Which currency would you sell? >>>")
        buy_curr = buy_curr.upper()
        if buy_curr == "UAH":
            print("You'll get: ", price * float(exchange_list[1]["sale"]))
        else:
            print("Unfortunately, this is not possible")
    elif curr == "RUR":
        buy_curr = input("Which currency would you sell? >>>")
        buy_curr = buy_curr.upper()
        if buy_curr == "UAH":
            print("You'll get: ", price * float(exchange_list[2]["sale"]))
        else:
            print("Unfortunately, this is not possible")
    elif curr == "BTC":
        buy_curr = input("Which currency would you sale? >>>")
        buy_curr = buy_curr.upper()
        if buy_curr == "USD":
            print("You'll get: ", price * float(exchange_list[3]["sale"]))
        else:
            print("Unfortunately, this is not possible")
    elif curr == "UAH":
        buy_curr = input("Which currency would you sell? >>>")
        buy_curr = buy_curr.upper()
        if buy_curr == "USD":
            print("You'll get: ", price * float(exchange_list[0]["sale"]))
        elif buy_curr == "EUR":
            print("You'll get: ", price * float(exchange_list[1]["sale"]))
        elif buy_curr == "RUR":
            print("You'll get: ", price * float(exchange_list[2]["sale"]))
        else:
            print("Unfortunately, this is not possible")
    else:
        print("Undefined currency")
