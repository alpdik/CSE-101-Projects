
A=[[1,2,3,6],[4,5,6,9],[7,8,9,5]]
B=[[1,2,3,6],[4,5,6,8],[7,8,9,7]]
C=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
def matrix_multi(A,B,C):
    for i in range(len(A)):
        for j in range(len(A[0])):
                C[i][j] = A[i][j] * B[i][j]
    return C
print(
matrix_multi(A,B,C)
)