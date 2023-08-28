import csv
import json
#import os
#print(os.getcwd())
with open ("top_subcribes.csv", mode = 'r', encoding= "utf-8") as file:
    #cách đọc file cvs:
    #cách 1:
    # for line in file:
    #     print(line.strip())

    # cách 2:
    csv_file = csv.DictReader(file)
    lst = list(csv_file)
    #print(json.dumps(lst,indent=4))
    for item in lst:
        print(item)
