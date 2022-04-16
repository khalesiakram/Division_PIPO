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
	sbox = [0, 13, 14, 15, 5, 8, 11, 10, 28, 19, 22, 21, 27, 20, 17, 18, 16, 31, 30, 29, 9, 4, 3, 2, 12, 1, 6, 7, 23, 24, 25, 26] #pipo (s5_2) 

	filename = cipher + "_Inequalities.txt"

	present = Reduce(filename, sbox)

	rine = present.InequalitySizeReduce()

	filename_result = cipher + "_Reduce_Inequalities.txt"

	fileobj = open(filename_result, "w")
	for l in rine:
		fileobj.write(str(l) + "\n")
	fileobj.close()
