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


"""
dump : ghi du lieu vao file json
dumps: chuyen doi mot list[dict] hay dict thanh mot chuoi
load : doc du lieu tu file json -> tra ve list[dict] hay dict
loads : chuyen doi mot chuoi co dang dict hay list[dict] thanh list[dict] hay dict tuong ung 
"""

import json
data = '{"name" : "Hieu", "Age" : 20}'
_dict = json.loads(data)
print(_dict)


"""
csv
DictReader - list[dict] 
writer(file) 
writerow
writerows
"""