num_list = []
print("Enter 5 numbers!")
for  i in  range(1, 6):
    x = int(input(f"Enter number {i} : "))
    num_list.append(x)
num_list_sign = []
for h in num_list:
    if h > 0:
        num_list_sign.append("\"Positive\"")
    if h < 0:
        num_list_sign.append("\"Negative\"")
    if h ==  0:
        num_list_sign.append("\"Neutral\"")
print(*num_list_sign, sep = ",")
    