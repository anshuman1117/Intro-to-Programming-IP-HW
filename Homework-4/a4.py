# a4.py
# Shloak Aggarwal - 2017107 - A2
# Anshuman Singh - 2017025 - A2
#################################

from math import inf as infinity
global mat

def swapRows(mat,row1,row2):

	temp = mat[row1]
	mat[row1] = mat[row2]
	mat[row2] = temp
	return mat

def RowTransformation(mat,x,row1,row2):
	for i in range(0,len(mat[0])):
		mat[row2][i] = mat[row2][i] - x*(mat[row1][i])
	return mat

def MatrixRank(mat):
	rows = len(mat)
	cols = len(mat[0])
	rank = min(rows,cols)
	i = 0
	while (i < rank):
		if(mat[i][i] != 0):

			for k in range (rows):
				if (k != i):
					x = mat[k][i]/mat[i][i]
					RowTransformation(mat,x,i,k)

		else: #elif(mat[i][i] == 0):
			if (i!=rank-1):
				for k in range (i+1,rows):
					if (mat[k][i] != 0):
						swapRows(mat,i,k)
						break
				r = 0
				for k in range (i+1,rows):
					if (mat[k][i] == 0):
						r = 1
					else:
						r = 0
						break

				if (r == 1 and i!=rank-1):
					for k in range (rows):
						mat[k][i], mat[k][i+1] = mat[k][i+1], mat[k][i]
					#rank-=1
				else:
					pass

			elif (i!=rank-1):
				for k in range (rows):
					mat[k][i], mat[k][i+1] = mat[k][i+1], mat[k][i]
				#rank-=1

			else:
				pass
		i+=1
		#print(mat)
	x = [];y = []
	for i in range(0,cols):
		x.append(0)
		y.append(0.0)
	for i in range(0,rows):
		if(mat[i] == x or mat[i] == y):
			rank -= 1

	return rank
