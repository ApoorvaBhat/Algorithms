import random
import timeit

def add(A, B):
    n = len(A)
    C = [[0.0 for j in range( n)] for i in range( n)]
    for i in range( n):
        for j in range( n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def naive(A, B):
    n = len(A)
    C = [[0.0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


def divide_conquer(A, B):
    """
        Implementation of the divide and conquer algorithm.
    """
    n = len(A)

    if n <= 1:
       return naive(A, B)
    else:
        # initializing the new sub-matrices
        mid = n/2
        a11 = [[0.0 for j in range( mid)] for i in range( mid)]
        a12 = [[0.0 for j in range( mid)] for i in range( mid)]
        a21 = [[0.0 for j in range( mid)] for i in range( mid)]
        a22 = [[0.0 for j in range( mid)] for i in range( mid)]

        b11 = [[0.0 for j in range( mid)] for i in range(mid)]
        b12 = [[0.0 for j in range(mid)] for i in range( mid)]
        b21 = [[0.0 for j in range( mid)] for i in range( mid)]
        b22 = [[0.0 for j in range( mid)] for i in range( mid)]

        # dividing the matrices in 4 sub-matrices:
        for i in range( mid):
            for j in range( mid):
                a11[i][j] = A[i][j]
                a12[i][j] = A[i][j + mid]
                a21[i][j] = A[i + mid][j]
                a22[i][j] = A[i + mid][j + mid]

                b11[i][j] = B[i][j]            # top left
                b12[i][j] = B[i][j + mid]    # top right
                b21[i][j] = B[i + mid][j]    # bottom left
                b22[i][j] = B[i + mid][j + mid] # bottom right

         # calculating c11,c12,c21,c22:

        c11 = add(divide_conquer(a11,b11),divide_conquer(a12,b21))  # c11 = a11*b11 + a12*b12
        c12 = add(divide_conquer(a11,b12),divide_conquer(a12,b22))  # c12 = a11*b12 + a12*b22
        c21 = add(divide_conquer(a21,b11),divide_conquer(a22,b21))  # c21 = a21*b11 + a22*b21
        c22 = add(divide_conquer(a21,b12),divide_conquer(a22,b22))  # c22 = a21*b12 + a22*b22

        # Grouping the results obtained in a single matrix:
        C = [[0.0 for j in range( n)] for i in range( n)]
        for i in range( mid):
            for j in range( mid):
                C[i][j] = c11[i][j]
                C[i][j + mid] = c12[i][j]
                C[i + mid][j] = c21[i][j]
                C[i + mid][j + mid] = c22[i][j]
        return C



#n=16
n = int(input("\n\nEnter the size of the matrix: "))
A = [[random.random() for i in range(n)] for j in range(n)]#; print("A",A)
B = [[random.random() for i in range(n)] for j in range(n)]#;print("B",B)

M2 = [[0.0 for i in range(n)] for j in range(n)]

start_time = timeit.default_timer() #depends on platform ; can give process time or wall time ; OS dependant
M2 = divide_conquer(A,B)
elapsed = timeit.default_timer() - start_time
print'time in sec:', round(elapsed,6)
#print "op matrix:",M2




