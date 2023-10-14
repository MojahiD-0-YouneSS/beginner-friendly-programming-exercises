a, b, z  = int(input(" Enter a : ")), int(input(" Enter b : ")), 0
z, a= a, b
b = z
del z
print("a = ", a, "b =", b)