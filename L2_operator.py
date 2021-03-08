# Source: https://www.w3schools.com/python/python_operators.asp

# 1. Python Arithmetic Operators
# 1.1. lấy phần dư của phép chia >> thường dùng kiểm tra phép chia hết.
print(4 % 2)

# 1.2. Giả sữ 7:3 = 2.333333
print(7/3)  # lấy kết quả của phép chia (2.3333333).
print(7//3)  # lấy kết quả của phép chia, sau đó lấy ra phần nguyên. (2)

# 2. Python Assignment Operators
number = 4

# 2.1. Tăng 3 đơn vị cho number.
number = number + 3  # Cách 1
number += 3  # Cách 2.

# 3. Comparison operator: trả về kết quả True/False
# 3.1. Kiểm tra 2 giá tri bằng nhau hay ko ?
print(3 == 3)  # trả về True.
print("1" == 1)  # tra về False, vì khác kiểu dữ liệu
print("bag" == "Bag")  # tra ve False, vì 2 chữ khác nhau chữ b.

# 3.2.1. Kiem tra 2 gia tri khác nhau hay ko ?
print(3 != 3)  # trả về False.
print("1" != 1)  # tra về True, vì khác kiểu dữ liệu
print("bag" != "Bag")  # tra ve True, vì 2 chữ khác nhau chữ b.

# 3.2.2. Kiem tra lớn hơn (>, >=) và nhỏ hơn (<, <=)
print("so sanh lon hon", 1 >= 1)
print("so sanh nhỏ hon", 2 <= 3)
print("so sanh hai chữ: ", "baf" >= "apple")  # true, vì theo order alphabet.

# 3.3. Logical Operator: AND, OR, NOT
# AND: nếu tất cả các so sanh đều là TRUE -> ket qua cuoi cùng là TRUE, còn lai la FALSE
is_positive_num = (1 > 0) and (2 >= -1)
print("is_positive_num: ", is_positive_num)

is_positive_num = (-1 > 0) and (2 > -1)
print("is_positive_num: ", is_positive_num)

# OR: nếu tất cả các so sanh đều là FALSE -> ket qua cuoi cùng là TRUE, còn lai la FALSE
is_valid = (4 % 2 == 0) or (5 / 1 > 6)
print("is valid: ", is_valid)

is_valid = (4 % 2 != 0) or (5 / 1 > 6)
print("is valid: ", is_valid)

# 3.4. Python Membership Operators  (sẽ coi lai trong bài array, tupple)
# kiểm tra 1 phần tử có thuộc hay ko thuộc vè 1 tập nào đó: trả về True/False
tap_hop_so = [1, 3, 6, 9]
print("so 5 có trong tap_hop_so? ", 5 in tap_hop_so)
print("so 5 KO có tồn tại trong tap_hop_so? ", 5 not in tap_hop_so)

tap_hop_trai_cay = ["apple", "banana", "coconut"]
print("trái 'apple' có nằm trong mảng ko? ", "apple" in tap_hop_trai_cay)

sentence = "hello! how are you"
print("chữ 'hello' có tồn tai trong senetence ko? ", "hello" in sentence)
print("chữ 'hello!how' có tồn tai trong senetence ko? ", "hello!how" in sentence)

# 3.5 Python Identity Operators (ít dùng hơn so với những operators trên.)
# Đoc them tại: https://www.w3schools.com/python/trypython.asp?filename=demo_oper_identity1
