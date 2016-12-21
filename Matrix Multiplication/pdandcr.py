from math import floor
import random
import timeit,time
from threading import Thread


class Return_Thread_Value(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs, Verbose)
        self._return = None

    def run(self):#starts thread
        if self._Thread__target is not None:
            self._return = self._Thread__target(*self._Thread__args, **self._Thread__kwargs)

    def join(self): # returns value returned by the function call.
        Thread.join(self)
        return self._return

def added_matrices(A, B):
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def naive(A, B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


def rec_divide_conquer2(A, B):

    n = len(A)

    if n <= 32:
        return naive(A, B)
    else:
        # initializing the new sub-matrices
        mid = n//2
        a11 = [[0 for j in range(0, mid)] for i in range(0, mid)]
        a12 = [[0 for j in range(0, mid)] for i in range(0, mid)]
        a21 = [[0 for j in range(0, mid)] for i in range(0, mid)]
        a22 = [[0 for j in range(0, mid)] for i in range(0, mid)]

        b11 = [[0 for j in range(0, mid)] for i in range(0, mid)]
        b12 = [[0 for j in range(0, mid)] for i in range(0, mid)]
        b21 = [[0 for j in range(0, mid)] for i in range(0, mid)]
        b22 = [[0 for j in range(0, mid)] for i in range(0, mid)]

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
        # calculating c11,c12,c21,c22:

        c11 = added_matrices(rec_divide_conquer2(a11,b11),rec_divide_conquer2(a12,b21))
        c12 = added_matrices(rec_divide_conquer2(a11,b12),rec_divide_conquer2(a12,b22))
        c21 = added_matrices(rec_divide_conquer2(a21,b11),rec_divide_conquer2(a22,b21))
        c22 = added_matrices(rec_divide_conquer2(a21,b12),rec_divide_conquer2(a22,b22))

        # Grouping the results obtained in a single matrix:
        C = [[0 for j in range(0, n)] for i in range(0, n)]
        for i in range(0, mid):
            for j in range(0, mid):
                C[i][j] = c11[i][j]
                C[i][j + mid] = c12[i][j]
                C[i + mid][j] = c21[i][j]
                C[i + mid][j + mid] = c22[i][j]
        return C


def rec_divide_conquer(A, B):

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


        thread1 = Return_Thread_Value(target=rec_divide_conquer2, args=(a11,b11,))
        thread1.start()
        a11b11 = thread1.join()

        thread2 = Return_Thread_Value(target=rec_divide_conquer2, args=(a12,b21,))
        thread2.start()
        a12b21 = thread2.join()

        thread3 = Return_Thread_Value(target=rec_divide_conquer2, args=(a11,b12,))
        thread3.start()
        a11b12 = thread3.join()

        thread4 = Return_Thread_Value(target=rec_divide_conquer2, args=(a12,b22,))
        thread4.start()
        a12b22 = thread4.join()

        thread5 = Return_Thread_Value(target=rec_divide_conquer2, args=(a21,b11,))
        thread5.start()
        a21b11 = thread5.join()

        thread6 = Return_Thread_Value(target=rec_divide_conquer2, args=(a22,b21,))
        thread6.start()
        a22b21 = thread6.join()

        thread7 = Return_Thread_Value(target=rec_divide_conquer2, args=(a21,b12,))
        thread7.start()
        a21b12 = thread7.join()

        thread8 = Return_Thread_Value(target=rec_divide_conquer2, args=(a22,b22,))
        thread8.start()
        a22b22 = thread8.join()

        # calculating c11,c12,c21,c22:

        c11 = added_matrices(a11b11,a12b21)  # c11 = a11*b11 + a12*b12
        c12 = added_matrices(a11b12,a12b22)  # c12 = a11*b12 + a12*b22
        c21 = added_matrices(a21b11,a22b21)  # c21 = a21*b11 + a22*b21
        c22 = added_matrices(a21b12,a22b22)  # c22 = a21*b12 + a22*b22

        # Grouping the results obtained in a single matrix:
        C = [[0 for j in range(0, n)] for i in range(0, n)]
        for i in range(0, mid):
            for j in range(0, mid):
                C[i][j] = c11[i][j]
                C[i][j + mid] = c12[i][j]
                C[i + mid][j] = c21[i][j]
                C[i + mid][j + mid] = c22[i][j]
    return C





def divide_conquer(A, B):

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

#Create Threads:
        thread1 = Return_Thread_Value(target=rec_divide_conquer, args=(a11,b11,))
        thread1.start()
        a11b11 = thread1.join()
        thread2 = Return_Thread_Value(target=rec_divide_conquer, args=(a12,b21,))
        thread2.start()
        a12b21 = thread2.join()

        thread3 = Return_Thread_Value(target=rec_divide_conquer, args=(a11,b12,))
        thread3.start()
        a11b12 = thread3.join()
        thread4 = Return_Thread_Value(target=rec_divide_conquer, args=(a12,b22,))
        thread4.start()
        a12b22 = thread4.join()

        thread5 = Return_Thread_Value(target=rec_divide_conquer, args=(a21,b11,))
        thread5.start()
        a21b11 = thread5.join()

        thread6 = Return_Thread_Value(target=rec_divide_conquer, args=(a22,b21,))
        thread6.start()
        a22b21 = thread6.join()

        thread7 = Return_Thread_Value(target=rec_divide_conquer, args=(a21,b12,))
        thread7.start()
        a21b12 = thread7.join()

        thread8 = Return_Thread_Value(target=rec_divide_conquer, args=(a22,b22,))
        thread8.start()
        a22b22 = thread8.join()
#Gets the return value from the function called.

        # calculating c11,c12,c21,c22:

        c11 = added_matrices(a11b11,a12b21)  # c11 = a11*b11 + a12*b12
        c12 = added_matrices(a11b12,a12b22)  # c12 = a11*b12 + a12*b22

        c21 = added_matrices(a21b11,a22b21)  # c21 = a21*b11 + a22*b21
        c22 = added_matrices(a21b12,a22b22)  # c22 = a21*b12 + a22*b22

        # Grouping the results obtained in a single matrix:
        C = [[0 for j in range(0, n)] for i in range(0, n)]
        for i in range(0, mid):
            for j in range(0, mid):
                C[i][j] = c11[i][j]
                C[i][j + mid] = c12[i][j]
                C[i + mid][j] = c21[i][j]
                C[i + mid][j + mid] = c22[i][j]
    return C



#n = 4
n = int(input("\n\nEnter the size of the matrix: "))
A = [[random.random() for i in range(n)] for j in range(n)]
B = [[random.random() for i in range(n)] for j in range(n)]
M4 = [[0 for i in range(n)] for j in range(n)]

start_time = timeit.default_timer() #depends on platform ; can give process time or wall time ; OS dependant
T4 = divide_conquer(A,B)
elapsed = timeit.default_timer() - start_time
print'time in sec:', round(elapsed,6)
#print "op matrix:",T4

