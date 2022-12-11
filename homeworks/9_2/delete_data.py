import export_data


def delete(id):
    list = export_data.export_data()
    list.pop(int(id) - 1)

    with open('phone.csv', 'w') as file:
        for i in list:
            file.write(','.join(i))
            file.write(f"\n")