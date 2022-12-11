def print_data(data):
    if len(data) > 0:
        print("Id".center(5), "Фамилия".center(20), "Имя".center(20), "Телефон".center(15), "Примечание".center(30))
        print("-"*85)
        for item in data:
            print(item[0].center(5) , item[1].center(20), item[2].center(20), item[3].center(15), item[4].center(30))
    else:
        print("Справочник пуст!")