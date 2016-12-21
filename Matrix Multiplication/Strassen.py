import random
import time,timeit

def naive(A, B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


def added_matrices(A, B):
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def difference(A, B):
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = A[i][j] - B[i][j]
    return C

def stra_mul(A,B):
       # c = [[ 0.0 for i in range(rhigh)]for j in range(rhigh)];#print(c)

        n = len(A)
        if n==1:
             return naive(A, B)



        #calculate the sum matrices
        mid = n//2
        a11 = [[0 for j in range( mid)] for i in range( mid)]
        a12 = [[0 for j in range( mid)] for i in range( mid)]
        a21 = [[0 for j in range( mid)] for i in range( mid)]
        a22 = [[0 for j in range( mid)] for i in range( mid)]

        b11 = [[0 for j in range( mid)] for i in range( mid)]
        b12 = [[0 for j in range( mid)] for i in range( mid)]
        b21 = [[0 for j in range( mid)] for i in range( mid)]
        b22 = [[0 for j in range( mid)] for i in range( mid)]

        aResult = [[0 for j in range(0, mid)] for i in range(0, mid)]
        bResult = [[0 for j in range(0, mid)] for i in range(0, mid)]


        # dividing the matrices in 4 sub-matrices:
        for i in range(0, mid):
            for j in range(0, mid):
                a11[i][j] = A[i][j]            # top left
                a12[i][j] = A[i][j + mid]    # top right
                a21[i][j] = A[i + mid][j]    # bottom left
                a22[i][j] = A[i + mid][j + mid] # bottom right

                b11[i][j] = B[i][j]            # top left
                b12[i][j] = B[i][j + mid]    # top right
                b21[i][j] = B[i + mid][j]    # bottom left
                b22[i][j] = B[i + mid][j + mid] # bottom right


        # Calculating p1 to p7:
        bResult = difference(b12, b22) # b12 - b22
        p1 = stra_mul(a11, bResult)  # p1 = (a11) * (b12 - b22)

        aResult = added_matrices(a11, a12)      # a11 + a12
        p2 = stra_mul(aResult, b22)  # p2 = (a11+a12) * (b22)

        aResult = added_matrices(a21, a22)      # a21 + a22
        p3 = stra_mul(aResult, b11)  # p3 = (a21+a22) * (b11)


        bResult = difference(b21, b11) # b21 - b11
        p4 =stra_mul(a22, bResult)   # p4 = (a22) * (b21 - b11)

        aResult = added_matrices(a11, a22)
        bResult = added_matrices(b11, b22)
        p5 = stra_mul(aResult, bResult) # p5 = (a11+a22) * (b11+b22)


        aResult = difference(a12, a22) # a12 - a22
        bResult = added_matrices(b21, b22)      # b21 + b22
        p6 = stra_mul(aResult, bResult) # p6 = (a12-a22) * (b21+b22)

        aResult = difference(a11, a21) # a11 - a21
        bResult = added_matrices(b11, b12)      # b11 + b12
        p7 = stra_mul(aResult, bResult) # p7 = (a11-a21) * (b11+b12)

        # calculating c21, c21, c11 e c22:


        c12 = added_matrices(p1, p2) # c12 = p1 + p2
        c21 = added_matrices(p3, p4)  # c21 = p3 + p4
        aResult = added_matrices(p5, p6) # p5 + p6
        bResult = added_matrices(aResult, p4) #
        c11 = difference(bResult, p2) # c11 = p5 + p6 + p4-p2
        aResult = added_matrices(p1, p5) # p1 + p5
        bResult = difference(aResult, p3) # p1 + p5-p3
        c22 = difference(bResult, p7) # c22 = p1 + p5-p3 -p7

        # Grouping the results obtained in a single matrix:
        C = [[0.0 for j in range( n)] for i in range( n)]
        for i in range(mid):
            for j in range( mid):
                C[i][j] = c11[i][j]
                C[i][j + mid] = c12[i][j]
                C[i + mid][j] = c21[i][j]
                C[i + mid][j + mid] = c22[i][j]
        return C


#n = 16

n = int(input("\n\nEnter the size of the matrix: "))
A= [[random.random()for i in range(n)] for j in range(n)]#;print "A",A
B= [[random.random() for i in range(n)] for j in range(n)]#;print "B",B


M3 = [[0.0 for i in range(n)] for j in range(n)]
start_time3 = timeit.default_timer() #depends on platform ; can give process time or wall time ; OS dependant
res2 = stra_mul(A,B)
elapsed = timeit.default_timer() - start_time3
print'time in sec:',round(elapsed,6)
#print"res2",res2




