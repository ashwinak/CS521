import csv

csv_file = open('a.txt','rb')
csv_reader = csv.reader(csv_file)
for row in csv_reader:
    print (row[0])

csv_file.close()
