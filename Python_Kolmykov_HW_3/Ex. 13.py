def pagination():
    import requests

    response_list = requests.get("http://jsonplaceholder.typicode.com/posts").json()
    try:
        i = 0
        while i < len(response_list):
            print(response_list[i])
            print(response_list[i + 1])
            print(response_list[i + 2])
            i += 3

            input(">>>")
    except IndexError:
        print("Pagination has been ended")
    else:
        print('All is ok')  # Это строка заработает, если я отниму 1 от длини списка на 7 строке


print(pagination())
