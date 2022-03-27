"""
the idea is in here https://www.youtube.com/watch?v=1ZGJzvkcLsA
just breath explanation is that we initially set
bounders and eah step move them untill there is
no way to move

inside while loop we have to make four simple steps

1) go through top row from left to right and 
append these elems to result arr after that
move top constraint down
2) go through right col form top to bottom and 
append these elems to result arr after that
move right constraint left
1) go through bottom row from right to left and 
append these elems to result arr after that
move bottom constraint up
1) go through left col from bottom to top and 
append these elems to result arr after that
move left constraint right

and again we have to do this untill borders
cross each other then we return result
"""

matrix = [[1,2,3],[4,5,6],[7,8,9]]

result = []

row_begin = 0
col_begin = 0
row_end = len(matrix) - 1 
col_end = len(matrix[0]) - 1

# the idea is go spirally
while row_begin <= row_end and col_begin <= col_end:
	# through top row (left to right)
	for i in range(col_begin, col_end + 1):
		result.append(matrix[row_begin][i])
	row_begin += 1

	# through right col (top to bottom)
	for i in range(row_begin, row_end + 1):
		result.append(matrix[i][col_end])
	col_end -= 1
		
	# through bottom row (right to left)
	if row_begin <= row_end:
		for i in range(col_end, col_begin - 1, -1):
			result.append(matrix[row_end][i])
		row_end -= 1

	# through left col (bottom to top)
	if col_begin <= col_end:
		for i in range(row_end, row_begin - 1, -1):
			result.append(matrix[i][col_begin])
		col_begin += 1

print(result)
