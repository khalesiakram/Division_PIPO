x0 = 0
x1 = 0
x2 = 0
x3 = 1
x4 = 0
x5 = 0
x6 = 0
x7 = 1
s51 = [0,9,23,28,5,26,19,14,8,1,29,22,15,18,27,4,20,31,3,10,17,12,7,24,25,6,13,16,30,21,11,2]
s3 = [4,7,5,0,3,2,1,6]
s52=[0,13,14,15,5,8,11,10,28,19,22,21,27,20,17,18,16,31,30,29,9,4,3,2,12,1,6,7,23,24,25,26]
#print(len(s51))
#####S51
s51_input_str = [str(x7),str(x6),str(x5),str(x4),str(x3)]
bina = "".join(s51_input_str)
deci = int(bina,2)
s51_out_dec = s51[deci]
s51_out_bin = bin(s51_out_dec)
if len(s51_out_bin) == 3:
    y3 = s51_out_bin[2]
    y4 = 0
    y5 = 0
    y6 = 0
    y7 = 0
if len(s51_out_bin) == 4:
    y3 = s51_out_bin[3]
    y4 = s51_out_bin[2]
    y5 = 0
    y6 = 0
    y7 = 0
if len(s51_out_bin) == 5:
    y3 = s51_out_bin[4]
    y4 = s51_out_bin[3]
    y5 = s51_out_bin[2]
    y6 = 0
    y7 = 0
if len(s51_out_bin) == 6:
    y3 = s51_out_bin[5]
    y4 = s51_out_bin[4]
    y5 = s51_out_bin[3]
    y6 = s51_out_bin[2]
    y7 = 0
if len(s51_out_bin) == 7:
    y3 = s51_out_bin[6]
    y4 = s51_out_bin[5]
    y5 = s51_out_bin[4]
    y6 = s51_out_bin[3]
    y7 = s51_out_bin[2]
#print((s51_out_bin))
#print("y3: ",y3,"y4: ",y4,"y5: ",y5,"y6: ",y6,"y7: ",y7)

####S3
s3_input_str = [str(x2),str(x1),str(x0)]
bina_3 = "".join(s3_input_str)
deci_3 = int(bina_3,2)
#print(deci_3)
s3_out_dec = s3[deci_3]
s3_out_bin = bin(s3_out_dec)
if len(s3_out_bin) == 3:
    y0 = s3_out_bin[2]
    y2 = 0
    y1 = 0
if len(s3_out_bin) == 4:
    y0 = s3_out_bin[3]
    y1 = s3_out_bin[2]
    y2 = 0
if len(s3_out_bin) == 5:
    y0 = s3_out_bin[4]
    y1 = s3_out_bin[3]
    y2 = s3_out_bin[2]
#print((s3_out_bin))
#print("y2: ",y2,"y1: ",y1,"y0: ",y0)

####
w2 = int(y0) ^ int(y4)
w3 = int(y1) ^ int(y7)
w1 = int(y2) ^ int(y3)
o5 = w2
o0 = w3
o6 = w1
#print("w3: ",w3,"w2: ",w2,"w1: ",w1)
####S5_2
s52_input_str = [str(w3),str(y6),str(y5),str(w2),str(w1)]
bina_52 = "".join(s52_input_str)
deci_52 = int(bina_52,2)
s52_out_dec = s52[deci_52]
s52_out_bin = bin(s52_out_dec)
#print("s52_out_bin: ",s52_out_bin)
if len(s52_out_bin) == 3:
    z1 = s52_out_bin[2]
    z2 = 0
    z3 = 0
    z4 = 0
    z5 = 0
if len(s52_out_bin) == 4:
    z1 = s52_out_bin[3]
    z2 = s52_out_bin[2]
    z3 = 0
    z4 = 0
    z5 = 0
if len(s52_out_bin) == 5:
    z1 = s52_out_bin[4]
    z2 = s52_out_bin[3]
    z3 = s52_out_bin[2]
    z4 = 0
    z5 = 0
if len(s52_out_bin) == 6:
    z1 = s52_out_bin[5]
    z2 = s52_out_bin[4]
    z3 = s52_out_bin[3]
    z4 = s52_out_bin[2]
    z5 = 0
if len(s52_out_bin) == 7:
    z1 = s52_out_bin[6]
    z2 = s52_out_bin[5]
    z3 = s52_out_bin[4]
    z4 = s52_out_bin[3]
    z5 = s52_out_bin[2]
o4 = z3
o3 = z4
print("o4: ",o4,"o3: ",o3)
#####
o1 = int(y0) ^ int(z1)
o7 = int(y1) ^ int(z2)
o2 = int(y2) ^ int(z5)
#print("o2: ",o2,"o7: ",o7,"o1: ",o1)

#####
output_str = [str(o7),str(o6),str(o5),str(o4),str(o3),str(o2),str(o1),str(o0)]
bina_output = "".join(output_str)
deci_output = int(bina_output,2)
hexa_output = hex(deci_output)
print("output" ,hexa_output)

print("o7: ",o7, "\n", "o6: ", o6, "\n", "o5: ", o5, "\n", "o4: ", o4,"\n" ,"o3: ", o3, "\n", "o2: ", o2, "\n", "o1: ", o1,"\n","o0: ",o0)



#print((s3_out_bin))
#print("y2: ",y2,"y1: ",y1,"y0: ",y0)


#binary = []
#for i in range(0,32):
 #   binary.append(bin(s51[i]))
#print(binary)