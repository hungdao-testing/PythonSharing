# A. For Else
# Reference : https://www.w3schools.com/python/gloss_python_for_else.asp

# 1. Giải thích code:
for x in range(6):  # cho x trong khoảng từ 0 -> 5
    print(x)        # print x
# sau khi x chạy đến 5, bắt đầu execute(chạy) câu lênh bên trong else.
else:
    print("Finally Finished")

# VD_A1: (Giả lập) sau khi user login 3 lần thất bại, gửi email
print("=========================")
is_successful_msg = True

for i in range(3):
    print(f"Login lần {i+1} thất bại")
else:
    print("Bạn đăng nhập 3 lần thất bại, chúng tôi đã gửi email!!!")

# B. For Break: Dùng chung với if, và chấm dứt vòng lặp ở bên ngoài chứa nó.

# Kiểm tra phần tử "blue" có trong mảng hay ko, nếu có dừng ngay!!!
print("=========================")

colors = ['red', 'green', 'blue', 'yellow']
for x in colors:
    if x == 'blue':
        break
    print(x)

# C. For - If - Break -  Else
# Lấy ví dụ VD_A1, nếu user thử chỉ 1 lần đăng nhập thành công => in câu "đăng nhập thành công", và thoát.
# Nếu sau 3 lần, in "thất bại"

print("=========================")
is_successful_msg = False

for i in range(3):
    print(f"Login lần {i+1}")
    if is_successful_msg:
        print("Đăng nhập thành công")
        break
else:
    print("Bạn đăng nhập 3 lần thất bại!!!")

# Notes: Trường hợp Loop chấm dứt bởi "Break" thì câu lênh trong else ko được thực thi
print("=========================")
is_successful_msg = True

for i in range(3):
    print(f"Login lần {i+1}")
    if is_successful_msg:
        print("Đăng nhập thành công")
        # do break được thực hiện / gọi (executed/ triggered) >>> vòng lap chấm dứt >>> else ko được thuc hien
        break
else:
    print("Bạn đăng nhập 3 lần thất bại!!!")


# ============= Exercise =================
# 1. Display a message “Done” after successful execution of for loop in range (1,10)

# 2. Given a list, iterate it, and display numbers divisible by five, and if
# you find a number greater than 150, stop the loop iteration.
# list_to_search = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# Reference: https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/
