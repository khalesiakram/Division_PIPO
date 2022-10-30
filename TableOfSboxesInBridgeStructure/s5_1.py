x3 = 1
x4 = 1
x5 = 1
x6 = 1
x7 = 1
#S5_1
x5 ^= x7 & x6
x4 ^= x3 & x5
x7 ^= x4
x6 ^= x3
x3 ^= x4 | x5
x5 ^= x7
x4 ^= x5 & x6

print("x7: ",x7, "\n", "x6: ", x6, "\n", "x5: ", x5, "\n", "x4: ", x4)
my_List = [str(x7),str(x6),str(x5),str(x4),str(x3)]
bina = "".join(my_List)
print("bin: ", bina)
deci = int(bina,2)
print("dec:" , deci)
hexa = hex(deci)
print("hex:" ,hexa)