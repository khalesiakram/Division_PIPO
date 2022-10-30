# Algorithm 1 presented in paper "Applyint MILP Method to Searching Integral 
# Distinguishers based on Division Property for 6 Lightweight Block Ciphers"
# Regarding to the paper, please refer to https://eprint.iacr.org/2016/857
# For more information, feedback or questions, pleast contact at xiangzejun@iie.ac.cn

# Implemented by Xiang Zejun, State Key Laboratory of Information Security, 
# Institute Of Information Engineering, CAS



from reducelin import Reduce

if __name__ == "__main__":

	cipher = "PRESENT" #This applied for PIPO cipher
	#sbox = [0xc, 0x5, 0x6, 0xb, 0x9, 0x0, 0xa, 0xd, 0x3, 0xe, 0xf, 0x8, 0x4, 0x7, 0x1, 0x2]
	sbox = [0, 9, 23, 28, 5, 26, 19, 14, 8, 1, 29, 22, 15, 18, 27, 4, 20, 31, 3, 10, 17, 12, 7, 24, 25, 6, 13, 16, 30, 21, 11, 2] #pipo (s5_1) 

	filename = cipher + "_Inequalities.txt"

	present = Reduce(filename, sbox)

	rine = present.InequalitySizeReduce()

	filename_result = cipher + "_Reduce_Inequalities.txt"

	fileobj = open(filename_result, "w")
	for l in rine:
		fileobj.write(str(l) + "\n")
	fileobj.close()
