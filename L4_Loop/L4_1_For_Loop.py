################## A. Range: https://www.w3schools.com/python/ref_func_range.asp #########################
# range(start, stop, step)
check_range_3_arguments_1 = range(0, 3, 1)

# check_range_3_arguments_2 = range(1, 3, 0)  # ERROR: step must not be zero

# lấy kết quả từ 1 đến 3; nếu ko có đối số step, default step value = 1
check_range_2_argument_1 = range(1, 4)

# trường hợp 1 đối số, start = 0, stop = 5, step = 0 ==> lay ket qua từ 0 ->4
check_range_1_argument = range(5)


for x in check_range_1_argument:
    print(x)

################# B. Loop qua chuỗi ký tự #######################
string_one = "hello world"
for string in string_one:
    print(string)

################# C. Loop qua Mảng (list) #######################
list_one = ["hello world", 1, True]
for string in list_one:
    print(string)

################# D. TIP #######################
# Thông thường For-loop phải có nội dung bên trong, nhưng nếu mình muốn define trước mà ko muốn chương trình báo lỗi
# mình dùng keyword trong Python `pass` để thông báo For-loop này là rỗng và ko báo lỗi

for x in range(2):
    pass


################# E. Exercise #######################
# 1. Print các số từ trong khoảng [10, 100]
# 2. Print các số chẳn trong khoảng [0, 10]
# 3. Print các số lẻ trong khoảng [0, 10]
# 4. Nhập 1 số nguyên từ màn hình, và in bảng cửu chương cho số đó, với định dạng (format):
#  1 * 1 = 1
#  1 * 2 = 2
#  .....
