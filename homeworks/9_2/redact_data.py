from search_data import search_data


def redact(id,data):
    item = search_data(id,data)
    print("Id".center(5), "Фамилия".center(20), "Имя".center(20), "Телефон".center(15), "Примечание".center(30))
    print("-"*85)
    print(item[0].center(5) , item[1].center(20), item[2].center(20), item[3].center(15), item[4].center(30))

    n = input('Введите назвние данных для редактирования :')
    m = input('Введите значение : ')
    if n == 'Фамилия': item[1] = m
    elif n == 'Имя': item[2] = m
    elif n == 'Телефон': item[3] = m
    elif n == 'Примечание': item[4] = m
    with open('phone.csv', 'w') as file:
        for i in data:
            file.write(','.join(i))
            file.write(f"\n")

    # list.pop(id - 1)
    # print(list)

    # with open('phone.csv', 'w') as file:
    #     for i in list:
    #         file.write(','.join(i))
    #         file.write(f"\n")