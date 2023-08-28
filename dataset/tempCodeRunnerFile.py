import csv

with open ("top_subcribes.csv", mode = 'r', encoding= "utf-8") as file:
    #cách đọc file cvs:
    #cách 1:
    # for line in file:
    #     print(line.strip())

    # cách 2:
    csv_file = csv.DictReader(file)
    print(csv_file)