import os, sys


def get_cur(matrix_score,c_row,c_col):


	tmp = matrix_score[c_row - 1][c_col - 1]
	direction = LU
	if s1[c_col -1] == s2[c_row - 1]:
		tmp = tmp + 1
	else:
		tmp = tmp - 1

	if tmp < matrix_score[c_row - 1][c_col] - 1:
		tmp = matrix_score[c_row - 1][c_col] - 1
		direction = UP


	if tmp < matrix_score[c_row][c_col - 1] - 1:
		tmp = matrix_score[c_row][c_col - 1] - 1
		direction = LEFT


	if tmp <= 0:
		direction = NO
		tmp = 0
	
	return (tmp,direction)



def fill_m(matrix_score,matrix_arrow,row,col,s1,s2):
	for i in range(1,row):
		for j in range(1,col):
			direction = NO
			(cur,direction) = get_cur(matrix_score,i,j)
			matrix_score[i][j] = cur
			matrix_arrow[i][j] = direction



def get_max(matrix_score,row,col):


	max_row = row - 1 
	max_col = col - 1 
	max_score = matrix_score[max_row][max_col]

	for i in range(max_row,-1,-1):
		for j in range(max_col,-1,-1):
			if max_score < matrix_score[i][j]:
				max_score = matrix_score[i][j]
				max_row = i
				max_col = j
	return (max_row,max_col)



def result(matrix_score,matrix_arrow,row,col,s1,s2):


	result1 = []
	result2 = []

	(max_row,max_col) = get_max(matrix_score,row,col)


	cur_row = max_row
	cur_col = max_col
	while matrix_arrow[cur_row][cur_col] != NO:
		if matrix_arrow[cur_row][cur_col] == UP:
			result1.append("_")
			cur_row -= 1
		elif matrix_arrow[cur_row][cur_col] == LEFT:
			result1.append(s1[cur_col-1])
			cur_col -= 1
		elif matrix_arrow[cur_row][cur_col] == LU:
			result1.append(s1[cur_col-1])
			cur_col -= 1
			cur_row -= 1


	cur_row = max_row
	cur_col = max_col
	while matrix_arrow[cur_row][cur_col] != NO:
		if matrix_arrow[cur_row][cur_col] == UP:
			result2.append(s2[cur_row-1])
			cur_row -= 1
		elif matrix_arrow[cur_row][cur_col] == LEFT:
			result2.append("_")
			cur_col -= 1
		elif matrix_arrow[cur_row][cur_col] == LU:
			result2.append(s2[cur_row-1])
			cur_col -= 1
			cur_row -= 1

	return (result1,result2)


def output(list_result):
	length = len(list_result)
	for i in range(length,0,-1):
		sys.stdout.write(list_result[i-1])
	print




NO = 0
UP = 1
LEFT = 2
LU = 3


fileHandle1 = open("seqS.fasta","r");
fileHandle2 = open("seqT.fasta","r");
s1 = fileHandle1.read()
s2 = fileHandle2.read()
fileHandle1.close()
fileHandle2.close()


l1 = len(s1) - 1	
l2 = len(s2) - 1


M_ROW = l2 + 1
M_COL = l1 + 1

matrix_score = [[0 for i in range(M_COL)] for j in range(M_ROW)]
matrix_arrow = [[0 for i in range(M_COL)] for j in range(M_ROW)]


fill_m(matrix_score,matrix_arrow,M_ROW,M_COL,s1,s2)

(result1,result2) = result(matrix_score,matrix_arrow,M_ROW,M_COL,s1,s2)

print(output(result1))
print(output(result2))
