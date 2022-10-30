"""
x_i_63,x_i_62,....x_i_0 denote the input to the (i+1)-th round.
"""

from gurobipy import *

import time

class Pipo:
	def __init__(self, Round, activebits):
		self.Round = Round
		self.activebits = activebits
		self.blocksize = 64
		self.filename_model = "Pipo_" + str(self.Round) + "_" + str(self.activebits) + ".lp"
		self.filename_result = "result_" + str(self.Round) + "_" + str(self.activebits) + ".txt"
		fileobj = open(self.filename_model, "w")
		fileobj.close()
		fileboj = open(self.filename_result, "w")
		fileobj.close()

	# Linear inequalities for the PIPO Sbox S5_1
	S51_T=[[1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 0],\
	[-1, 0, -1, -1, 0, 1, 0, 1, 1, 2, 0],\
	[-1, -4, -5, -1, -6, 3, 6, 3, 7, -2, 8],\
	[2, 3, 4, 0, 4, -5, -8, 6, -10, -9, 13],\
	[1, -1, 0, 1, 0, -1, 1, -2, -2, 0, 3],\
	[0, 0, 5, 3, 1, -1, -2, -4, -2, -3, 4],\
	[2, 1, 1, 0, 5, -3, -1, -3, -2, -5, 5],\
	[0, -1, -1, -3, -2, 1, 2, 1, 3, 2, 2],\
	[1, 1, 5, 4, 0, -3, -2, -3, -3, -2, 3],\
	[-1, 0, -1, -3, -2, 1, 2, -3, -1, 0, 8],\
	[2, 0, 0, 3, 0, -1, -1, -1, -2, -1, 2],\
	[-1, 0, 4, 0, 3, -2, -3, -2, -1, -3, 5],\
	[-2, -1, -3, 0, -1, 1, 1, 1, 2, 1, 3],\
	[-1, -2, -3, -3, -2, 1, 0, 1, 1, 2, 6],\
	[1, 3, 1, 0, 3, -2, -3, -2, -1, -3, 3],\
	[-1, -1, 0, 0, -2, 4, 2, 4, 3, 2, 0],\
	[2, 1, 0, 3, 0, -1, -1, -2, -2, -1, 2],\
	[3, 1, 3, 2, 2, -4, -2, -2, -4, -2, 3],\
	[-1, 2, -1, 0, -2, -2, 2, 2, 0, -1, 5],\
	[0, -1, -1, 0, 0, 1, 1, 1, 2, 1, 0],\
	[0, -1, -1, -2, -1, 0, -1, 1, 0, 1, 4],\
	[0, 0, 3, 2, 1, -4, -2, -1, -2, -1, 4],\
	[-1, -1, 0, 0, 0, 2, 1, 2, 1, 2, 0],\
	[2, 1, -1, 0, 0, -2, -1, 1, 0, -1, 3]]
	NUMBER1 = 11

	# Linear inequalities for the PIPO Sbox S5_2
	S52_T=[[1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 0],\
	[-1, -1, 0, -1, 0, 1, 1, 2, 1, 0, 0],\
	[-1, -2, -1, 0, -1, -1, 1, 1, 0, 1, 3],\
	[0, 3, 0, 0, 1, -1, -1, -2, -1, -1, 2],\
	[-1, -2, -1, 0, -2, 2, 1, 1, 3, 2, 1],\
	[4, 1, 4, 0, 4, -1, -2, -6, -5, -5, 6],\
	[3, 4, 4, 2, -1, -4, -6, -5, -7, 2, 8],\
	[-1, -1, 0, -1, 0, 1, -1, 0, 1, 0, 2],\
	[1, 3, 0, 4, 1, -2, -4, -1, -5, -2, 5],\
	[0, -1, -1, -2, -1, 1, 3, 3, 2, 1, 0],\
	[-1, -1, 0, 0, 0, 1, 1, 1, 0, -1, 1],\
	[1, 1, 1, 0, 0, -1, -1, -1, 0, -1, 1],\
	[0, -2, -2, -1, 0, 1, 1, 2, 3, 2, 1],\
	[-3, 0, -1, -2, -3, -1, -1, 1, -4, 3, 11],\
	[-1, 2, 0, 0, 1, -1, -1, -1, 0, -2, 3],\
	[3, 1, 1, 3, 2, -2, -3, -2, -4, -2, 3],\
	[-1, 3, 0, 2, 1, -1, -2, -2, -2, -1, 3],\
	[0, 0, 0, -1, -1, 0, 2, 2, 1, 1, 0],\
	[1, 0, 0, 1, 1, 1, -2, -1, -3, -2, 4],\
	[1, 0, 2, 0, 2, -1, -1, -2, -1, -2, 2]]
	NUMBER2 = 11

	# Linear inequalities for the PIPO Sbox S3
	S3_T=[[1, 1, 1, -1, -1, -1, 0],\
	[-2, -1, -1, 2, 3, 3, 0],\
	[0, -2, -2, 1, 1, -1, 3],\
	[0, 0, 0, -1, -1, 1, 1],\
	[0, 0, 2, -1, -1, -1, 1],\
	[-1, 0, -1, 1, 0, -1, 2]]
	NUMBER3 = 7

	def CreateObjectiveFunction(self):
		"""
		Create objective function of the MILP model
		"""
		fileobj = open(self.filename_model, "a")
		fileobj.write("Minimize\n")
		eqn = []
		for i in range(0,64):
			eqn.append("x" + "_" + str(self.Round) + "_" + str(i))
		temp = " + ".join(eqn)
		fileobj.write(temp)
		fileobj.write("\n")
		fileobj.close()


	def CreateVariables(self,n,x):
		"""
		Generate the variables used in the model.
		"""
		variable = []
		for i in range(0, 64):
			variable.append(x + "_" + str(n) + "_" + str(i))
		return variable

	def CreateVariables8(self,n,x):
		"""
		Generate the variables used in the model.
		"""
		variable = []
		for i in range(0, 8):
			variable.append(x + "_" + str(n) + "_" + str(i))
		return variable

	def CreateVariables24(self,n,x):
		"""
		Generate the variables used in the model.
		"""
		variable = []
		for i in range(0, 24):
			variable.append(x + "_" + str(n) + "_" + str(i))
		return variable

	def CreateVariables52(self,n, x, m):
		"""
		Generate the variables used in the model.
		"""
		variable = []
		for i in range(0, 8):
			variable.append(x + "_" + str(n) + "_" + str(i + m))
		return variable
		
	def ConstraintsBySbox51(self, variable1, variable2):
		"""
		Generate the constraints by sbox layer (S5_1).
		"""
		fileobj = open(self.filename_model,"a")
		for k in range(0,8):
			for coff in Pipo.S51_T:
				temp = []
				for u in range(0,5):
					temp.append(str(coff[4 - u]) + " " + variable1[(u * 8) + 24 + k])
				for v in range(0,5):
					temp.append(str(coff[9 - v]) + " " + variable2[(v * 8) + 24 + k])
				temp1 = " + ".join(temp)
				temp1 = temp1.replace("+ -", "- ")
				s = str(-coff[Pipo.NUMBER1 - 1])
				s = s.replace("--", "")
				temp1 += " >= " + s
				fileobj.write(temp1)
				fileobj.write("\n")
		fileobj.close() 
	
	def ConstraintsBySbox3(self, variable1, variable2):
		"""
		Generate the constraints by sbox layer (S3).
		"""
		fileobj = open(self.filename_model,"a")
		for k in range(0,8):
			for coff in Pipo.S3_T:
				temp = []
				for u in range(0,3):
					temp.append(str(coff[2 - u]) + " " + variable1[(u * 8) + k])
				for v in range(0,3):
					temp.append(str(coff[5 - v]) + " " + variable2[(v * 8) + k])
				temp1 = " + ".join(temp)
				temp1 = temp1.replace("+ -", "- ")
				s = str(-coff[Pipo.NUMBER3 - 1])
				s = s.replace("--", "")
				temp1 += " >= " + s
				fileobj.write(temp1)
				fileobj.write("\n")
		fileobj.close()
	
	def ConstraintsBySbox52(self, w3, y6, y5, w2, w1, z5, z4, z3, z2, z1):
		"""
		Generate the constraints by sbox layer (S5_2).
		"""
		fileobj = open(self.filename_model,"a")
		for i in range(0,8):
			for coff in Pipo.S52_T:
				temp = []			
				temp.append(str(coff[0]) + " " + w3[i])
				temp.append(str(coff[1]) + " " + y6[i])
				temp.append(str(coff[2]) + " " + y5[i])
				temp.append(str(coff[3]) + " " + w2[i])
				temp.append(str(coff[4]) + " " + w1[i])
				temp.append(str(coff[5]) + " " + z5[i])
				temp.append(str(coff[6]) + " " + z4[i])
				temp.append(str(coff[7]) + " " + z3[i])
				temp.append(str(coff[8]) + " " + z2[i])
				temp.append(str(coff[9]) + " " + z1[i])	
				temp1 = " + ".join(temp)
				temp1 = temp1.replace("+ -", "- ")
				s = str(-coff[Pipo.NUMBER2 - 1])
				s = s.replace("--", "")
				temp1 += " >= " + s
				fileobj.write(temp1)
				fileobj.write("\n")
		fileobj.close()

	def ConstraintsByCopy(self, x, a, b, shift):
		"""
		Generate the constraints by copy operation.
        """
		fileobj = open(self.filename_model,"a")
		for i in range(0,8):
			temp = []
			temp.append(x[i + shift])
			temp.append(a[i + shift])
			temp.append(b[i + shift])
			s = " - ".join(temp)
			s += " = 0"
			fileobj.write(s)
			fileobj.write("\n")
		fileobj.close()

	def ConstraintsByCopy1(self, x, a, b):
		"""
		Generate the constraints by copy operation.
        """
		fileobj = open(self.filename_model,"a")
		for i in range(0,8):
			temp = []
			temp.append(x[i])
			temp.append(a[i])
			temp.append(b[i])
			s = " - ".join(temp)
			s += " = 0"
			fileobj.write(s)
			fileobj.write("\n")
		fileobj.close()
	
	def ConstraintsByCopy2(self, x, a, b):
		"""
		Generate the constraints by copy operation.
        """
		fileobj = open(self.filename_model,"a")
		for i in range(0,8):
			temp = []
			temp.append(x[i + 8])
			temp.append(a[i + 8])
			temp.append(b[i + 8])
			s = " - ".join(temp)
			s += " = 0"
			fileobj.write(s)
			fileobj.write("\n")
		fileobj.close()

	def ConstraintsByCopy3(self, x, a, b):
		"""
		Generate the constraints by copy operation.
        """
		fileobj = open(self.filename_model,"a")
		for i in range(0,8):
			temp = []
			temp.append(x[i + 16])
			temp.append(a[i + 16])
			temp.append(b[i + 16])
			s = " - ".join(temp)
			s += " = 0"
			fileobj.write(s)
			fileobj.write("\n")
		fileobj.close()

	def ConstraintsByXOR1(self, a, b, w2):
		"""
		Generate the constraints by copy operation.
        """
		fileobj = open(self.filename_model,"a")
		for i in range(0,8):
			temp = []
			temp.append(w2[i])
			temp.append(a[i])
			temp.append(b[i + 32])
			s = " - ".join(temp)
			s += " = 0"
			fileobj.write(s)
			fileobj.write("\n")
		fileobj.close()

	def ConstraintsByXOR2(self, a, b, w3):
		"""
		Generate the constraints by copy operation.
        """
		fileobj = open(self.filename_model,"a")
		for i in range(0,8):
			temp = []
			temp.append(w3[i])
			temp.append(a[i + 8])
			temp.append(b[i + 56])
			s = " - ".join(temp)
			s += " = 0"
			fileobj.write(s)
			fileobj.write("\n")
		fileobj.close()

	def ConstraintsByXOR3(self, a, b, w1):
		"""
		Generate the constraints by copy operation.
        """
		fileobj = open(self.filename_model,"a")
		for i in range(0,8):
			temp = []
			temp.append(w1[i])
			temp.append(a[i + 16])
			temp.append(b[i + 24])
			s = " - ".join(temp)
			s += " = 0"
			fileobj.write(s)
			fileobj.write("\n")
		fileobj.close()

	def ConstraintsByXOR4(self, b, z, o):
		"""
		Generate the constraints by copy operation.
        """
		fileobj = open(self.filename_model,"a")
		for i in range(0,8):
			temp = []
			temp.append(o[i])
			temp.append(b[i])
			temp.append(z[i])
			s = " - ".join(temp)
			s += " = 0"
			fileobj.write(s)
			fileobj.write("\n")
		fileobj.close()

	def ConstraintsByXOR5(self, b, z, o):
		"""
		Generate the constraints by copy operation.
        """
		fileobj = open(self.filename_model,"a")
		for i in range(0,8):
			temp = []
			temp.append(o[i])
			temp.append(b[i + 8])
			temp.append(z[i])
			s = " - ".join(temp)
			s += " = 0"
			fileobj.write(s)
			fileobj.write("\n")
		fileobj.close()

	def ConstraintsByXOR6(self, b, z, o):
		"""
		Generate the constraints by copy operation.
        """
		fileobj = open(self.filename_model,"a")
		for i in range(0,8):
			temp = []
			temp.append(o[i])
			temp.append(b[i + 16])
			temp.append(z[i])
			s = " - ".join(temp)
			s += " = 0"
			fileobj.write(s)
			fileobj.write("\n")
		fileobj.close()

	@staticmethod
	def LinearLaryer(s0, s1, s2, s3, s4, s5, s6, s7):
		"""
		Linear layer of Pipo.
		"""
		array = [[" " for i in range(0,8)] for j in range(0,64)]
		for i in range(0,8):
			array[i] = s0[i]
		for i in range(0,8):
			array[i + 8] = s1[(i + 7) % 8]
		for i in range(0,8):
			array[i + 16] = s2[(i + 4) % 8]
		for i in range(0,8):
			array[i + 24] = s3[(i + 3) % 8]
		for i in range(0,8):
			array[i + 32] = s4[(i + 6) % 8]
		for i in range(0,8):
			array[i + 40] = s5[(i + 5) % 8]
		for i in range(0,8):
			array[i + 48] = s6[(i + 1) % 8]
		for i in range(0,8):
			array[i + 56] = s7[(i + 2) % 8]
		return array


	def Constraint(self):
		"""
		Generate the constraints used in the MILP model.
		"""
		assert(self.Round >= 1)
		fileobj = open(self.filename_model, "a")
		fileobj.write("Subject To\n")
		fileobj.close()

		x_in = self.CreateVariables(0, "x")	#input of S5_1 and S3
		#x_out = self.CreateVariables(1, "x")

		y = self.CreateVariables(0, "y")	#output of S5_1 and S3

		a = self.CreateVariables24(0, "a") 	#copy output of S3
		b = self.CreateVariables24(0, "b") 	#copy output of S3

		w1 = self.CreateVariables8(0, "w1")	#output of XOR1
		w2 = self.CreateVariables8(0, "w2")	#output of XOR1
		w3 = self.CreateVariables8(0, "w3")	#output of XOR1

		c = self.CreateVariables8(0, "c")	#copy w2 for input S5_2
		x5 = self.CreateVariables52(1, "x", 40)	#copy w2 for output: x5 / row = 5: x_r_40 to x_r_47
		#d = self.CreateVariables8(i, "d")	#copy w2 for output: s5 / row = 5

		e = self.CreateVariables8(0, "e")	#copy w3 for input S5_2
		x0 = self.CreateVariables52(1, "x", 0)	#copy w3 for output: x0 / row = 0: x_r_0 to x_r_7
		#f = self.CreateVariables8(i, "f")	#copy w3 for output: s0 / row = 0

		g = self.CreateVariables8(0, "g")	#copy w1 for input S5_2
		x6 = self.CreateVariables52(1, "x", 48)	#copy w1 for output: x6 / row = 6 x_r_48 to x_r_55
		#h = self.CreateVariables8(i, "h")	#copy w1 for output: s6 / row = 6

		y6 = self.CreateVariables52(0, "y", 48) #y_r_48 to y_r_55
		y5 = self.CreateVariables52(0, "y", 40)	#y_r_40 to y_r_47
		z5 = self.CreateVariables8(0, "z5")		#output of S5_2
		#z4 = self.CreateVariables8(i, "z4")		#output of S5_2 / output: s3 / row = 3
		x3 = self.CreateVariables52(1, "x", 24)		#output of S5_2 / output: x3 / row = 3
		#z3 = self.CreateVariables8(i, "z3")		#output of S5_2 / output: s4 / row = 4
		x4 = self.CreateVariables52(1, "x", 32)		#output of S5_2 / output: x4 / row = 4
		z2 = self.CreateVariables8(0, "z2")		#output of S5_2
		z1 = self.CreateVariables8(0, "z1")		#output of S5_2

		x1 = self.CreateVariables52(1, "x", 8)		#output of XOR2 / output: x1 / row = 1
		x7 = self.CreateVariables52(1, "x", 56)		#output of XOR2 / output: x7 / row = 7
		x2 = self.CreateVariables52(1, "x", 16)		#output of XOR2 / output: x2 / row = 2		
		
		if self.Round == 1:
			self.ConstraintsBySbox51(x_in, y)
			self.ConstraintsBySbox3(x_in, y)

			y = self.CreateVariables24(0, "y") 	#output of S3: y_r_0 to y_r_23
			self.ConstraintsByCopy(y, a, b, 0) 	#copy output of S3
			self.ConstraintsByCopy(y, a, b, 8) 	#copy output of S3
			self.ConstraintsByCopy(y, a, b, 16) #copy output of S3

			#a = self.CreateVariables(0, "a") 	#a_r_0 to a_r_63  
			y = self.CreateVariables(0, "y") 	#y_r_0 to y_r_63
			self.ConstraintsByXOR1(a, y, w2)    #S3 XOR S5_1
			self.ConstraintsByXOR2(a, y, w3)	#S3 XOR S5_1
			self.ConstraintsByXOR3(a, y, w1)	#S3 XOR S5_1

			self.ConstraintsByCopy(w2, c , x5, 0)
			self.ConstraintsByCopy(w3, e , x0, 0)
			self.ConstraintsByCopy(w1, g , x6, 0)

			self.ConstraintsBySbox52(e, y6, y5, c, g, z5, x3, x4, z2, z1) #S5_2

			self.ConstraintsByXOR4(b, z1, x1)	#b_r_0 to b_r_7 XOR z1_r_0 to z1_r_7 = x1_r_0 to x1_r_7
			self.ConstraintsByXOR5(b, z2, x7)	#b_r_8 to b_r_15 XOR z2_r_0 to z2_r_7 = x7_r_0 to x7_r_7
			self.ConstraintsByXOR6(b, z5, x2)	#b_r_16 to b_r_23 XOR z5_r_0 to z5_r_7 = x2_r_0 to x2_r_7
			#omit the last linear laye

		else:
			self.ConstraintsBySbox51(x_in, y)
			self.ConstraintsBySbox3(x_in, y)

			y = self.CreateVariables24(0, "y") 	#output of S3: y_r_0 to y_r_23
			self.ConstraintsByCopy(y, a, b, 0) 	#copy output of S3
			self.ConstraintsByCopy(y, a, b, 8) 	#copy output of S3
			self.ConstraintsByCopy(y, a, b, 16) #copy output of S3

			#a = self.CreateVariables(0, "a") 	#a_r_0 to a_r_63  
			y = self.CreateVariables(0, "y") 	#y_r_0 to y_r_63
			self.ConstraintsByXOR1(a, y, w2)    #S3 XOR S5_1
			self.ConstraintsByXOR2(a, y, w3)	#S3 XOR S5_1
			self.ConstraintsByXOR3(a, y, w1)	#S3 XOR S5_1

			self.ConstraintsByCopy(w2, c , x5, 0)
			self.ConstraintsByCopy(w3, e , x0, 0)
			self.ConstraintsByCopy(w1, g , x6, 0)

			self.ConstraintsBySbox52(e, y6, y5, c, g, z5, x3, x4, z2, z1) #S5_2

			self.ConstraintsByXOR4(b, z1, x1)	#b_r_0 to b_r_7 XOR z1_r_0 to z1_r_7 = x1_r_0 to x1_r_7
			self.ConstraintsByXOR5(b, z2, x7)	#b_r_8 to b_r_15 XOR z2_r_0 to z2_r_7 = x7_r_0 to x7_r_7
			self.ConstraintsByXOR6(b, z5, x2)	#b_r_16 to b_r_23 XOR z5_r_0 to z5_r_7 = x2_r_0 to x2_r_7
			
			for i in range(1, self.Round):
				x_in = Pipo.LinearLaryer(x0, x1, x2, x3, x4, x5, x6, x7)	

				y = self.CreateVariables(i, "y")	#output of S5_1 and S3

				a = self.CreateVariables24(i, "a") 	#copy output of S3
				b = self.CreateVariables24(i, "b") 	#copy output of S3

				w1 = self.CreateVariables8(i, "w1")	#output of XOR1
				w2 = self.CreateVariables8(i, "w2")	#output of XOR1
				w3 = self.CreateVariables8(i, "w3")	#output of XOR1

				c = self.CreateVariables8(i, "c")	#copy w2 for input S5_2
				x5 = self.CreateVariables52((i + 1), "x", 40)	#copy w2 for output: x5 / row = 5: x_r_40 to x_r_47
		

				e = self.CreateVariables8(i, "e")	#copy w3 for input S5_2
				x0 = self.CreateVariables52((i + 1), "x", 0)	#copy w3 for output: x0 / row = 0: x_r_0 to x_r_7
		

				g = self.CreateVariables8(i, "g")	#copy w1 for input S5_2
				x6 = self.CreateVariables52((i + 1), "x", 48)	#copy w1 for output: x6 / row = 6 x_r_48 to x_r_55
		

				y6 = self.CreateVariables52(i, "y", 48) #y_r_48 to y_r_55
				y5 = self.CreateVariables52(i, "y", 40)	#y_r_40 to y_r_47
				z5 = self.CreateVariables8(i, "z5")		#output of S5_2	
				x3 = self.CreateVariables52((i + 1), "x", 24)	#output of S5_2 / output: x3 / row = 3
				x4 = self.CreateVariables52((i + 1), "x", 32)	#output of S5_2 / output: x4 / row = 4
				z2 = self.CreateVariables8(i, "z2")		#output of S5_2
				z1 = self.CreateVariables8(i, "z1")		#output of S5_2

				x1 = self.CreateVariables52((i + 1), "x", 8)		#output of XOR2 / output: x1 / row = 1
				x7 = self.CreateVariables52((i + 1), "x", 56)		#output of XOR2 / output: x7 / row = 7
				x2 = self.CreateVariables52((i + 1), "x", 16)		#output of XOR2 / output: x2 / row = 2

				self.ConstraintsBySbox51(x_in, y)
				self.ConstraintsBySbox3(x_in, y)

				y = self.CreateVariables24(i, "y") 	#output of S3: y_r_0 to y_r_23
				self.ConstraintsByCopy(y, a, b, 0) 	#copy output of S3
				self.ConstraintsByCopy(y, a, b, 8) 	#copy output of S3
				self.ConstraintsByCopy(y, a, b, 16) #copy output of S3

				#a = self.CreateVariables(0, "a") 	#a_r_0 to a_r_63   
				y = self.CreateVariables(i, "y") 	#y_r_0 to y_r_63
				self.ConstraintsByXOR1(a, y, w2)    #S3 XOR S5_1
				self.ConstraintsByXOR2(a, y, w3)	#S3 XOR S5_1
				self.ConstraintsByXOR3(a, y, w1)	#S3 XOR S5_1

				self.ConstraintsByCopy(w2, c , x5, 0)
				self.ConstraintsByCopy(w3, e , x0, 0)
				self.ConstraintsByCopy(w1, g , x6, 0)

				self.ConstraintsBySbox52(e, y6, y5, c, g, z5, x3, x4, z2, z1) #S5_2

				self.ConstraintsByXOR4(b, z1, x1)	#b_r_0 to b_r_7 XOR z1_r_0 to z1_r_7 = x1_r_0 to x1_r_7
				self.ConstraintsByXOR5(b, z2, x7)	#b_r_8 to b_r_15 XOR z2_r_0 to z2_r_7 = x7_r_0 to x7_r_7
				self.ConstraintsByXOR6(b, z5, x2)	#b_r_16 to b_r_23 XOR z5_r_0 to z5_r_7 = x2_r_0 to x2_r_7
				#omit the last linear laye	
			
				
	def VariableBinary(self):
		"""
		Specify the variable type.
		"""
		fileobj = open(self.filename_model, "a")
		fileobj.write("Binary\n")
		for i in range(0, (self.Round + 1)):
			for j in range(0,64):
				fileobj.write("x_" + str(i) + "_" + str(j))
				fileobj.write("\n")

		for i in range(0, self.Round):
			for j in range(0,64):
				fileobj.write("y_" + str(i) + "_" + str(j))
				fileobj.write("\n")
			for j in range(0,24):
				fileobj.write("a_" + str(i) + "_" + str(j))
				fileobj.write("\n")
				fileobj.write("b_" + str(i) + "_" + str(j))
				fileobj.write("\n")
			for j in range(0,8):
				fileobj.write("w1_" + str(i) + "_" + str(j))
				fileobj.write("\n")
				fileobj.write("w2_" + str(i) + "_" + str(j))
				fileobj.write("\n")
				fileobj.write("w3_" + str(i) + "_" + str(j))
				fileobj.write("\n")
				fileobj.write("c_" + str(i) + "_" + str(j))
				fileobj.write("\n")
				fileobj.write("e_" + str(i) + "_" + str(j))
				fileobj.write("\n")
				fileobj.write("g_" + str(i) + "_" + str(j))
				fileobj.write("\n")
				fileobj.write("z1_" + str(i) + "_" + str(j))
				fileobj.write("\n")
				fileobj.write("z2_" + str(i) + "_" + str(j))
				fileobj.write("\n")
				fileobj.write("z5_" + str(i) + "_" + str(j))
				fileobj.write("\n")
		fileobj.write("END")
		fileobj.close()

	def Init(self):
		"""
		Generate the constraints introduced by the initial division property.
		"""
		variableout = self.CreateVariables(0, "x")
		fileobj = open(self.filename_model, "a")
		eqn = []
		for i in range(0, self.activebits):
			temp = variableout[63 - i] + " = 1"
			fileobj.write(temp)
			fileobj.write("\n")
		for i in range(self.activebits, 64):
			temp = variableout[63 - i] + " = 0"
			fileobj.write(temp)
			fileobj.write("\n")
		fileobj.close()

	def MakeModel(self):
		"""
		Generate the MILP model of Pipo given the round number and activebits.
		"""
		self.CreateObjectiveFunction()
		self.Constraint()
		self.Init()
		self.VariableBinary()

	def WriteObjective(self, obj):
		"""
		Write the objective value into filename_result.
		"""
		fileobj = open(self.filename_result, "a")
		fileobj.write("The objective value = %d\n" %obj.getValue())
		eqn1 = []
		eqn2 = []
		for i in range(0, self.blocksize):
			u = obj.getVar(i)
			if u.getAttr("x") != 0:
				eqn1.append(u.getAttr('VarName'))
				eqn2.append(u.getAttr('x'))
		length = len(eqn1)
		for i in range(0,length):
			s = eqn1[i] + "=" + str(eqn2[i])
			fileobj.write(s)
			fileobj.write("\n")
		fileobj.close()

	def SolveModel(self):
		"""
		Solve the MILP model to search the integral distinguisher of Pipo.
		"""
		time_start = time.time()
		m = read(self.filename_model)
		counter = 0
		set_zero = []
		global_flag = False
		while counter < self.blocksize:
			m.optimize()
			# Gurobi syntax: m.Status == 2 represents the model is feasible.
			if m.Status == 2:
				obj = m.getObjective()
				if obj.getValue() > 1:
					global_flag = True
					break
				else:
					fileobj = open(self.filename_result, "a")
					fileobj.write("************************************COUNTER = %d\n" % counter)
					fileobj.close()
					self.WriteObjective(obj)
					for i in range(0, self.blocksize):
						u = obj.getVar(i)
						temp = u.getAttr('x')
						if temp == 1:
							set_zero.append(u.getAttr('VarName'))
							u.ub = 0
							m.update()
							counter += 1
							break
			# Gurobi syntax: m.Status == 3 represents the model is infeasible.
			elif m.Status == 3:
				global_flag = True
				break
			else:
				print("Unknown error!")

		fileobj = open(self.filename_result, "a")		
		if global_flag:
			fileobj.write("\nIntegral Distinguisher Found!\n\n")
			print("Integral Distinguisher Found!\n")
		else:
			fileobj.write("\nIntegral Distinguisher do NOT exist\n\n")
			print("Integral Distinguisher do NOT exist\n")

		fileobj.write("Those are the coordinates set to zero: \n")
		for u in set_zero:
			fileobj.write(u)
			fileobj.write("\n")
		fileobj.write("\n")
		time_end = time.time()
		fileobj.write(("Time used = " + str(time_end - time_start)))
		fileobj.close()


