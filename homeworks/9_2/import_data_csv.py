import csv
import export_data

list = export_data.export_data()
# print(type(list))
print(list)

with open('eggs.csv', 'w', newline='') as csvfile:

    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in list:
        spamwriter.writerow(i)
    # spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])