x0 = 0
x1 = 1
x2 = 0

#S3
x2 ^= x1 & x0
x0 ^= x2 | x1
x1 ^= x2 | x0
#if x2 == 1:
 #   x2 = 0
#else:
 #   x2 = 1
x2 ^= 1
print("x2: ", x2, "\n", "x1: ", x1, "\n", "x0: ", x0)
my_List = [str(x2),str(x1),str(x0)]
bina = "".join(my_List)
print("bin: ", bina)
deci = int(bina,2)
print("dec: ", deci)
hexa = hex(deci)
print("hex:" ,hexa)