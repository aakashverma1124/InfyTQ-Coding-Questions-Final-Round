#
#	Problem Statement:
#	The input is a N x N matrix where some of the items in the matrix are 0.
#	If any of the items are 0, then set that item's entire row and column to 0.
#	items that are not 0 will be represented by an integer.
#
#	Video Link: 
#
#	Instagram: http://instagram.com/aakashverma1102
#	LinkedIn: https://www.linkedin.com/in/aakashverma1124/
#



def set_zero(matrix, n):
	zero_rows = [False] * n
	zero_cols = [False] * n
	
	for i in range(n):
		for j in range(n):
			if matrix[i][j] == 0:
				zero_rows[i] = True
				zero_cols[j] = True

	for i in range(n):
		if zero_rows[i] is True:
			for col in range(n):
				matrix[i][col] = 0

	for i in range(n):
		if zero_cols[i] is True:
			for row in range(n):
				matrix[row][i] = 0

	return matrix

if __name__ == '__main__':
	
	n = int(input())
	arr = []
	for i in range(n):
		row = list(map(int, input().split()))
		arr.append(row)

	ans = set_zero(arr, n)

	for i in range(n):
		for j in range(n):
			print(ans[i][j], end = " ")
		print()

