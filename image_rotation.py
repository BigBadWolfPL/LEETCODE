from typing import List

matrix = [[1,2,3],[4,5,6],[7,8,9]]
out = [[7,4,1],[8,5,2],[9,6,3]]

#for m, o in zip(matrix, out):
#    print(m, o)

def rotate(matrix: List[List[int]]) -> None:
    length = len(matrix)
    for i in range(length):
        for j in range(i+1, length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for layer in matrix:
        layer.reverse()
    for row in matrix:
        print(row)










rotate(matrix)