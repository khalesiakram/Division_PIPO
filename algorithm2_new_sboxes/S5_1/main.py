# Algorithm 2 presented in paper "Applyint MILP Method to Searching Integral 
# Distinguishers based on Division Property for 6 Lightweight Block Ciphers"
# Regarding to the paper, please refer to https://eprint.iacr.org/2016/857
# For more information, feedback or questions, pleast contact at xiangzejun@iie.ac.cn

# Implemented by Xiang Zejun, State Key Laboratory of Information Security, 
# Institute Of Information Engineering, CAS



from sbox import Sbox

if __name__ == "__main__":

	# PIPO Sbox
	cipher = "PIPO"
	sbox = [0,9,23,28,5,26,19,14,8,1,29,22,15,18,27,4,20,31,3,10,17,12,7,24,25,6,13,16,30,21,11,2]
	present = Sbox(sbox)

	filename = cipher + "_DivisionTrails.txt"

	present.PrintfDivisionTrails(filename)
