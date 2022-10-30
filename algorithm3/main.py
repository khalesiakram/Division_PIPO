# Algorithm 3 presented in paper "Applyint MILP Method to Searching Integral 
# Distinguishers based on Division Property for 6 Lightweight Block Ciphers"
# Regarding to the paper, please refer to https://eprint.iacr.org/2016/857
# For more information, feedback or questions, pleast contact at xiangzejun@iie.ac.cn

# Implemented by Xiang Zejun, State Key Laboratory of Information Security, 
# Institute Of Information Engineering, CAS

from pipo import Pipo

if __name__ == "__main__":

	ROUND = int(input("Input the target round number: "))
	while not (ROUND > 0):
		print("Input a round number greater than 0.")
		ROUND = int(input("Input the target round number again: "))

	ACTIVEBITS = int(input("Input the number of acitvebits: "))
	while not (ACTIVEBITS < 64 and ACTIVEBITS > 0):
		print("Input a number of activebits with range (0, 64):")
		ACTIVEBITS = int(input("Input the number of acitvebits again: "))

	pipo = Pipo(ROUND, ACTIVEBITS)

	pipo.MakeModel()

	pipo.SolveModel()
