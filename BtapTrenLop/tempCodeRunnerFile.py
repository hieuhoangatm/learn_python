from decimal import Decimal, getcontext
import math
getcontext().prec = 50  # Số chữ số thập phân sau dấu chấm
getcontext().Emax = 999999999  # Đặt giới hạn độ lớn cao hơn
x = Decimal(str(3+math.isqrt(5)))
y = Decimal('1999999')

# Thực hiện phép tính số mũ
result = x ** y

# In kết quả
print(result)