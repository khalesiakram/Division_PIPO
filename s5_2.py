x3 = 1
x4 = 1
x5 = 1
x6 = 1
x7 = 1
#S5_2
t0 = x7
t1 = x3 
t2 = x4
x6 ^= t0 & x5
t0 ^= x6
x6 ^= t2 | t1
t1 ^= x5
x5 ^= x6 | t2
t2 ^= t1 & t0

print("x7: ",t0, "\n", "x6: ", x6, "\n", "x5: ", x5, "\n", "x4: ", t2, "\n","x3: ",t1)
my_List = [str(t0),str(x6),str(x5),str(t2),str(t1)]
bina = "".join(my_List)
print("bin: ", bina)
deci = int(bina,2)
print("dec:" , deci)
hexa = hex(deci)
print("hex:" ,hexa)