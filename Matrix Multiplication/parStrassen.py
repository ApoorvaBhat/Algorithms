import random
import time,timeit
from threading import Thread


class Return_Thread_Value(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs, Verbose)
        self._return = None

    def run(self):
        if self._Thread__target is not None:
            self._return = self._Thread__target(*self._Thread__args, **self._Thread__kwargs)

    def join(self):
        Thread.join(self)
        return self._return


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


def naive(A, B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def rec_strassen_mul2(A, B):
    """
        Implementation of the strassen_mul algorithm.
    """
    n = len(A)

    if n <= 32:
        return naive(A, B)
    else:
        # initializing the new sub-matrices
        mid = n/2
        a11 = [[0 for j in range(0, mid)] for i in range(0, mid)]
        a12 = [[0 for j in range(0, mid)] for i in range(0, mid)]
        a21 = [[0 for j in range(0, mid)] for i in range(0, mid)]
        a22 = [[0 for j in range(0, mid)] for i in range(0, mid)]

        b11 = [[0 for j in range(0, mid)] for i in range(0, mid)]
        b12 = [[0 for j in range(0, mid)] for i in range(0, mid)]
        b21 = [[0 for j in range(0, mid)] for i in range(0, mid)]
        b22 = [[0 for j in range(0, mid)] for i in range(0, mid)]

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
        prod1 = rec_strassen_mul2(added_matrices(a11, a22), added_matrices(b11, b22)) # prod1 = (a11+a22) * (b11+b22)

        prod2 = rec_strassen_mul2(added_matrices(a21, a22), b11)  #prod2 = (a21+a22) * (b11)

        prod3 = rec_strassen_mul2(a11, difference(b12, b22))  #prod3 = (a11) * (b12 - b22)

        prod4 = rec_strassen_mul2(a22, difference(b21, b11))   #prod4 = (a22) * (b21 - b11)

        prod5 = rec_strassen_mul2(added_matrices(a11, a12), b22)  #prod5 = (a11+a12) * (b22)

        prod6 = rec_strassen_mul2(difference(a21, a11), added_matrices(b11, b12)) #prod6 = (a21-a11) * (b11+b12)

        prod7 = rec_strassen_mul2(difference(a12, a22), added_matrices(b21, b22)) #prod7 = (a12-a22) * (b21+b22)

        # calculating c21, c21, c11 e c22:

        c11 = difference(added_matrices(added_matrices(prod1,prod4),prod7),prod5) # c11 = prod1 +prod4 -prod5 +prod7
        c12 = added_matrices(prod3,prod5) # c12 =prod3 +prod5
        c21 = added_matrices(prod2,prod4)  # c21 =prod2 +prod4
        c22 = difference(added_matrices(added_matrices(prod1,prod3),prod6),prod2) # c22 = prod1 +prod3 -prod2 +prod6

        # Grouping the results obtained in a single matrix:
        C = [[0 for j in range(0, n)] for i in range(0, n)]
        for i in range(0, mid):
            for j in range(0, mid):
                C[i][j] = c11[i][j]
                C[i][j + mid] = c12[i][j]
                C[i + mid][j] = c21[i][j]
                C[i + mid][j + mid] = c22[i][j]
        return C

def rec_strassen_mul(A, B):
    """
        Implementation of the strassen algorithm.
        """
    n = len(A)

    if n <= 32:
        return naive(A, B)
    else:
        # initializing the new sub-matrices
        mid = n/2
        a11 = [[0 for j in range(0, mid)] for i in range(0, mid)]
        a12 = [[0 for j in range(0, mid)] for i in range(0, mid)]
        a21 = [[0 for j in range(0, mid)] for i in range(0, mid)]
        a22 = [[0 for j in range(0, mid)] for i in range(0, mid)]

        b11 = [[0 for j in range(0, mid)] for i in range(0, mid)]
        b12 = [[0 for j in range(0, mid)] for i in range(0, mid)]
        b21 = [[0 for j in range(0, mid)] for i in range(0, mid)]
        b22 = [[0 for j in range(0, mid)] for i in range(0, mid)]

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

        # Calculating values of prod1 to prod7 by creating threads:
        resultA = added_matrices(a11, a22)
        resultB = added_matrices(b11, b22)
        thread1 =Return_Thread_Value(target=rec_strassen_mul2, args=(resultA,resultB,))
        thread1.start()

        resultA = added_matrices(a21, a22)
        thread2 =Return_Thread_Value(target=rec_strassen_mul2, args=(resultA,b11,))
        thread2.start()

        resultB = difference(b12, b22)
        thread3 =Return_Thread_Value(target=rec_strassen_mul2, args=(a11,resultB,))
        thread3.start()


        resultB = difference(b21, b11)
        thread4 =Return_Thread_Value(target=rec_strassen_mul2, args=(a22,resultB,))
        thread4.start()


        resultA = added_matrices(a11, a12)
        thread5 =Return_Thread_Value(target=rec_strassen_mul2, args=(resultA,b22,))
        thread5.start()


        resultA = difference(a21, a11)
        resultB = added_matrices(b11, b12)
        thread6 =Return_Thread_Value(target=rec_strassen_mul2, args=(resultA,resultB,))
        thread6.start()


        resultA = difference(a12, a22)
        resultB = added_matrices(b21, b22)
        thread7 = Return_Thread_Value(target=rec_strassen_mul2, args=(resultA,resultB,))
        thread7.start()


#get the return value from each function calls
        # prod1 = (a11+a22) * (b11+b22);#prod2 = (a21+a22) * (b11)#prod3 = (a11) * (b12 - b22)#prod4 = (a22) * (b21 - b11)
         #prod5 = (a11+a12) * (b22) #prod6 = (a21-a11) * (b11+b12)#prod7 = (a12-a22) * (b21+b22)

        prod1 = thread1.join();prod2 = thread2.join()
        prod3 = thread3.join();prod4 = thread4.join()
        prod5 = thread5.join();prod6 = thread6.join()
        prod7 = thread7.join()

        # calculating c21, c21, c11 e c22:
        # c11 = prod1 +prod4 -prod5 +prod7
        c11 = difference(added_matrices(added_matrices(prod1,prod4),prod7),prod5)
        c12 = added_matrices(prod3,prod5) # c12 =prod3 +prod5
        c21 = added_matrices(prod2,prod4)  # c21 =prod2 +prod4
        c22 = difference(added_matrices(added_matrices(prod1,prod3),prod6),prod2) # c22 = prod1 +prod3 -prod2 +prod6

        # Grouping the results obtained in a single matrix:
        C = [[0 for j in range(0, n)] for i in range(0, n)]
        for i in range(0, mid):
            for j in range(0, mid):
                C[i][j] = c11[i][j]
                C[i][j + mid] = c12[i][j]
                C[i + mid][j] = c21[i][j]
                C[i + mid][j + mid] = c22[i][j]
        return C




def strassen_mul(A, B):
    """
        Implementation of the strassen algorithm.
    """
    n = len(A)

    if n <= 32:
        return naive(A, B)
    else:
        # initializing the new sub-matrices
        mid = n/2
        a11 = [[0 for j in range(0, mid)] for i in range(0, mid)]
        a12 = [[0 for j in range(0, mid)] for i in range(0, mid)]
        a21 = [[0 for j in range(0, mid)] for i in range(0, mid)]
        a22 = [[0 for j in range(0, mid)] for i in range(0, mid)]

        b11 = [[0 for j in range(0, mid)] for i in range(0, mid)]
        b12 = [[0 for j in range(0, mid)] for i in range(0, mid)]
        b21 = [[0 for j in range(0, mid)] for i in range(0, mid)]
        b22 = [[0 for j in range(0, mid)] for i in range(0, mid)]

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

        # Calculating values of prod1 to prod7 by creating threads:
        resultA = added_matrices(a11, a22)
        resultB = added_matrices(b11, b22)
        thread1 =Return_Thread_Value(target=rec_strassen_mul, args=(resultA,resultB,))
        thread1.start()

        resultA = added_matrices(a21, a22)
        thread2 =Return_Thread_Value(target=rec_strassen_mul, args=(resultA,b11,))
        thread2.start()

        resultB = difference(b12, b22)
        thread3 =Return_Thread_Value(target=rec_strassen_mul, args=(a11,resultB,))
        thread3.start()


        resultB = difference(b21, b11)
        thread4 =Return_Thread_Value(target=rec_strassen_mul, args=(a22,resultB,))
        thread4.start()


        resultA = added_matrices(a11, a12)
        thread5 =Return_Thread_Value(target=rec_strassen_mul, args=(resultA,b22,))
        thread5.start()


        resultA = difference(a21, a11)
        resultB = added_matrices(b11, b12)
        thread6 =Return_Thread_Value(target=rec_strassen_mul, args=(resultA,resultB,))
        thread6.start()


        resultA = difference(a12, a22)
        resultB = added_matrices(b21, b22)
        thread7 = Return_Thread_Value(target=rec_strassen_mul, args=(resultA,resultB,))
        thread7.start()


#get the return value from each function calls
        # prod1 = (a11+a22) * (b11+b22);#prod2 = (a21+a22) * (b11)#prod3 = (a11) * (b12 - b22)#prod4 = (a22) * (b21 - b11)
         #prod5 = (a11+a12) * (b22) #prod6 = (a21-a11) * (b11+b12)#prod7 = (a12-a22) * (b21+b22)

        prod1 = thread1.join();prod2 = thread2.join()
        prod3 = thread3.join();prod4 = thread4.join()
        prod5 = thread5.join();prod6 = thread6.join()
        prod7 = thread7.join()

        # calculating c21, c21, c11 e c22:
        # c11 = prod1 +prod4 -prod5 +prod7
        c11 = difference(added_matrices(added_matrices(prod1,prod4),prod7),prod5)
        c12 = added_matrices(prod3,prod5) # c12 =prod3 +prod5
        c21 = added_matrices(prod2,prod4)  # c21 =prod2 +prod4
        c22 = difference(added_matrices(added_matrices(prod1,prod3),prod6),prod2) # c22 = prod1 +prod3 -prod2 +prod6

        # Grouping the results obtained in a single matrix:
        C = [[0 for j in range(0, n)] for i in range(0, n)]
        for i in range(0, mid):
            for j in range(0, mid):
                C[i][j] = c11[i][j]
                C[i][j + mid] = c12[i][j]
                C[i + mid][j] = c21[i][j]
                C[i + mid][j + mid] = c22[i][j]
        return C

#n= 2
n = int(input("\n\nEnter the size of the matrix: "))
A = [[random.random() for i in range(n)] for j in range(n)]
B = [[random.random() for i in range(n)] for j in range(n)]


M5 = [[0 for i in range(n)] for j in range(n)]
start_time = timeit.default_timer() #depends on platform ; can give process time or wall time ; OS dependant
T5 = strassen_mul(A,B)
elapsed = timeit.default_timer() - start_time
print'time in sec:',round(elapsed,6)
#print "op matrix:",T5
