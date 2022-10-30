# Algorithm 2 presented in paper "Applyint MILP Method to Searching Integral 
# Distinguishers based on Division Property for 6 Lightweight Block Ciphers"
# Regarding to the paper, please refer to https://eprint.iacr.org/2016/857
# For more information, feedback or questions, pleast contact at xiangzejun@iie.ac.cn

# Implemented by Xiang Zejun, State Key Laboratory of Information Security, 
# Institute Of Information Engineering, CAS



from sbox import Sbox

if __name__ == "__main__":

	# PIPO Sbox S5_2
	cipher = "PIPO"
	sbox = [0, 13, 14, 15, 5, 8, 11, 10, 28, 19, 22, 21, 27, 20, 17, 18, 16, 31, 30, 29, 9, 4, 3, 2, 12, 1, 6, 7, 23, 24, 25, 26]
	present = Sbox(sbox)

	filename = cipher + "_DivisionTrails.txt"

	present.PrintfDivisionTrails(filename)
