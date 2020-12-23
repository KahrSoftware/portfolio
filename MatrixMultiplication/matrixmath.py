'''
matrixmath.py
A library of naive matrix operations for use in a neural net. Not very efficient.
Justin Kahr
'''

def matrix_add(A, B):
    if(len(A) != len(B) or len(A[0]) != len(B[0])):
        print("Matrix Add Incompatible Matrix Size")
        return -1
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matrix_basis_add(A, B):
    return [[ A[i][j] + B[0][j] for j in range(len(A[0]))] for i in range(len(A))]

def matrix_elem_mult(A, B):
    return [[A[i][j]*B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matrix_mult(A, B):
    if(len(A[0]) != len(B)):
        print("Matrix Mult Incompatible Matrix Size")
        return -1
    return [[sum(a*b for a,b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

def matrix_scalar_mult(alpha, A):
    return [[alpha*A[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matrix_transpose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

def vector_dot(A, B):
    if(len(A) != len(B)):
        print("Vector Dot Inccompativle Matrix Size")
        return -1
    return sum(A[i]*B[i] for i in range(len(A)))
