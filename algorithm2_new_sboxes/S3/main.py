# Algorithm 2 presented in paper "Applyint MILP Method to Searching Integral 
# Distinguishers based on Division Property for 6 Lightweight Block Ciphers"
# Regarding to the paper, please refer to https://eprint.iacr.org/2016/857
# For more information, feedback or questions, pleast contact at xiangzejun@iie.ac.cn

# Implemented by Xiang Zejun, State Key Laboratory of Information Security, 
# Institute Of Information Engineering, CAS



from sbox import Sbox

if __name__ == "__main__":

	# PIPO Sbox S3
	cipher = "PIPO"
	sbox = [4,7,5,0,3,2,1,6]
	present = Sbox(sbox)

	filename = cipher + "_DivisionTrails.txt"

	present.PrintfDivisionTrails(filename)
