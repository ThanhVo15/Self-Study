# Imnport thư viện
import math
# #Thực hành buổi 1 22/12/2023

# # Nhập dữ liệu vào bằng str
# print("Mời bạn nhập dữ liệu:")
# x = input()
# print(type(x))
# # Nhập dữ liệu vào bằng kiểu int
# x = int(input("Mời bạn nhập giá trị gì đó vô:"))
# print("Bạn đã nhập giá trị:", x)
# print("Gía trị của bạn có kiểu dữ liệu là:", type(x))

# #Thực hành buổi 2 23/12/2023
# print('-'* 20)
# print('{0:^4} {1:>15}'.format('STT', 'Giá tri'))
# print('-'* 20)
# print('{0:>4} {1:>15}'.format(1, 10**10)) #Căn phải
# print('{0:^4} {1:>15}'.format(2, 10**9)) #Căn trái
# print('{0:<4} {1:>15}'.format(3, 10**8)) # Căn giữa
# print('{0:^4} {1:>15}'.format(4, 10**7))
# print('{0:^4} {1:>15}'.format(5, 10**6))
# print('{0:^4} {1:>15}'.format(6, 10**5))
# print('{0:^4} {1:>15}'.format(7, 10**4))
# print('{0:^4} {1:>15}'.format(8, 10**3))
# print('{0:^4} {1:>15}'.format(9, 10**2))
# print('{0:^4} {1:>15}'.format(10, 10**1))
# print('-'* 20)

# #**Đề bài:** Nhập bán kính đường tròn r. Tính và xuất chu vi, diện tích đường tròn tương ứng

# r = float(input("Mời bạn nhập bán kính đường tròn:"))
# cv = round(r*2*math.pi, 3)
# s = round(math.pi*r, 3)
# print("Chu vi của đường tròn là:", cv)
# print("Diện tích đường tròn là:", s)

# # **Đề bài:** Nhập vào số giây bất kỳ t. Tính và xuất ra dạng Gio:Phut:Giay
# t = int(input("Mời bạn nhập số giây:"))
# hour = (t//3600)%24
# minute = (t%3600)//60
# second = (t%3600)%60
# print('{0}:{1}:{2}'.format(hour, minute, second))

# # 1.11 Bài tập rèn luyện: Tính điểm trung bình
# diem_toan = float(input("Moi ban nhap diem mon toan:"))
# diem_ly = float(input("Moi ban nhap diem mon ly:"))
# diem_hoa = float(input("Moi ban nhap diem mon hoa:"))
# diem_trung_binh = (diem_toan + diem_ly + diem_hoa)/3
# print("Diem trung binh cua ban la:", round(diem_trung_binh, 2))

# if diem_trung_binh >= 8.0:
#     print("Chuc mung ban la hoc sinh gioi!")
# elif 8.0> diem_trung_binh >= 6.5:
#     print("Chuc mung ban hoc sinh kha!")
# elif 6.5 > diem_trung_binh >= 5.0:
#     print("Chuc mung ban hoc sinh kem!") 
# else:
#     print("Chuc mung ban se o lai lop!")

# # Thực hành if else như một phép gán
# a = int(input("Mời bạn nhập số cần kiểm tra:"))
# d = a/2
# b = a//2

# c = "Số chẵn" if b == d else "Số lẻ"
# print(c)

# # **Đề bài:** Nhập vào một năm bất kỳ, kiểm tra năm đó có phải năm nhuần hay không. Biết rằng: Năm nhuần là năm chia hết cho 4 nhưng không chia hết cho 100 hoặc chia hết cho 400
# nam = int(input("Nhap nam can kiem tra:"))
# kiem_tra = nam/4
# kiem_tra2 = nam//4
# kiem_tra3 = nam/100
# kiem_tra4 = nam//100
# if kiem_tra == kiem_tra2 and kiem_tra3 != kiem_tra4:
#     print("Nam nhuan")
# else: 
#     print("Nam khong nhuan")

# year = int(input("Moi ban nhap nam can kiem tra:"))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print("Nam nhuan")
# else:
#     print("Nam khong nhuan")








