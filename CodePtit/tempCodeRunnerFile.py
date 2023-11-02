from datetime import datetime
ngaynhan = input()
ngaytra = input()
ngay1_obj = datetime.strptime(ngaynhan, "%d/%m/%Y")
ngay2_obj = datetime.strptime(ngaytra, "%d/%m/%Y")
delta = ngay2_obj - ngay1_obj
print(delta.days)