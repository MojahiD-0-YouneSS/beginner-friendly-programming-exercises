num_list = []
for  i in  range(1, 6):
    x = int(input("Enter 5 numbers : "))
    num_list.append(x)
sum = 0
for h in num_list:
    sum += h
average = sum / 5
print(average)
    