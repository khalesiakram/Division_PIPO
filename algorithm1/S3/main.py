# Algorithm 1 presented in paper "Applyint MILP Method to Searching Integral 
# Distinguishers based on Division Property for 6 Lightweight Block Ciphers"
# Regarding to the paper, please refer to https://eprint.iacr.org/2016/857
# For more information, feedback or questions, pleast contact at xiangzejun@iie.ac.cn

# Implemented by Xiang Zejun, State Key Laboratory of Information Security, 
# Institute Of Information Engineering, CAS



from reducelin import Reduce

if __name__ == "__main__":

	cipher = "PRESENT" #This applied for PIPO cipher
	sbox = [4 ,7 ,5 ,0 ,3, 2, 1, 6] #pipo cipher

	filename = cipher + "_Inequalities.txt"

	present = Reduce(filename, sbox)

	rine = present.InequalitySizeReduce()

	filename_result = cipher + "_Reduce_Inequalities.txt"

	fileobj = open(filename_result, "w")
	for l in rine:
		fileobj.write(str(l) + "\n")
	fileobj.close()
