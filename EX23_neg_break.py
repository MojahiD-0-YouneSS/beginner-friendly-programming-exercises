sum = 0
for  i in range(1, 100):
    x = int(input("Enter a number : "))
    if x > 0:
        sum += x
    elif x < 0:
        break
    else:
        x = 0
print("The sum is",sum)
