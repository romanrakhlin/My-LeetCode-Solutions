"""
the main idea is that we cant just rotate given matrix
this is impossible in terms of efficienc etc
but there is another approach to rotate it

watch Nick White's video if u want more details:
https://www.youtube.com/watch?v=SA867FvqHrM

breathly we can do it in two steps:
1) reverse it by diagonals
2) reverse it horizontally
try if u want on paper and u ll see that it works!
"""

matrix = [[1,2,3],[4,5,6],[7,8,9]]

n = len(matrix)

# 1
for i in range(0, n):
	for j in range(i, n):
		matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# 2
for i in range(0, n):
	matrix[i] = matrix[i][::-1]

print(matrix)