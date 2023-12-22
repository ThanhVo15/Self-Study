# 1. First Lesson (2:30 a.m. 21/12/20230)
## 1.1 Các kiểu dữ liệu cơ bản trong Python
- **Int:** Kiểu số nguyên ( Không có chứa dấu chấm thập phân), có thể là các số dương hoặc âm
Ví dụ: 113, -114
- **float:** Kiểu số thực ( có chứa dấu chấm thập phân), có thể là số dương hoặc âm
Ví dụ: 5.2, 7,3
- **Kiểu complex:** Kiểu số phức,
    - Vd 1: z = 2+3j thì 2 là phần thực, 3 là phần ảo (j là từ khóa để đánh dấu phần ảo)
    - Vd 2: z = complex(2,3) thì 2 là phần thực, 3 là phần ảo
    - Khi xuất kết quả ta có thể xuất ra bằng các cú pháp:
        - print("Phần thực:",z.real) ==> Phần thực: 2
        - print("Phần ảo:", z.imag) ==> Phần ảo: 3
- **Kiểu str:** Kiểu chuỗi, để trong nháy đôi hoặc nháy đơn
Ví dụ: "Obama", "Thành Đẹp Trai"
- **Kiểu bool:** Kiểu luận lý, để lưu True hoặc False
Ví dụ: t1: True
        t2: False
## 1.2 Khai báo biến trong Python
- Khác với C, C++ thì Python đầu vào dữ liệu không cần phải nhập kiểu dữ liệu. Python sẽ tự động nhận diện và gán biến. 
- Trong Python sử dụng **type()** để xem kiểu dữ liệu
    Ví dụ: x = 5
    print(type(x))
## 1.3 Cách xóa biến
x ="Thanhdeptrai"
print(x)
**del x**
## 1.4 Ghi chú khi lập trình
### 1.4.1 Vì sao nên ghi chú khi lập trình?
- Thể hiện tính chuyên nghiệp của Lập trình viên. Nếu không thì khả năng bị loại khi sinh việc là cực cao. 
-> Giỏi không đi đôi với cẩu thả
- Dễ dàng cho Lập trình viên và teamate đọc lại sau này
### 1.4.2 Ghi chú 1 dòng
- dùng dấu # để ghi chú 1 dòng
### 1.4.3 Ghi chú nhiều dòng
- Dùng dầu ''' để khi chú nhiều dòng
## 1.5 Các toán tử thường dùng trong Python
### 1.5.1 Toán tử số học cơ bản
![Alt text](image-2.png)
### 1.5.2 Toán tử gán
![Alt text](image-3.png)
### 1.5.3 Toán tử so sánh
![Alt text](image-4.png)
### 1.5.4 Toán tử Logic
![Alt text](image-5.png)
### 1.5.5 Độ ưu tiên toán tử
Dùng ngoặc () để ưu tiên nhóm nào làm trước
### 1.6 Cách nhập liệu từ bàn phím trong Python
- Nhập bằng input(), đầu ra hiểu bằng chuỗi. 
**Ví dụ 1:** Cách nhập thông thường
print("Mời bạn nhập str:")
x = input()
**Ví dụ 2:** Cách nhập định dạng luôn kiểu của giá trị nhập 
x = int(input())
x = float(input())

Đang dừng ở video 8
Pass giải nén: http://nhasachtinhoc.blogspot.com