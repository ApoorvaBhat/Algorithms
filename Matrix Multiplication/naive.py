
import timeit
import random
def naive(a,b):
        n = len(a)
        c = [[0.0 for i in range(n)] for j in range(n)];#print(c)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    c[i][j] += a[i][k] * b[k][j]

        return c




n = 4
A=[[random.random()for i in range(n)]for j in range(n)];print "A in main",A
B =[[random.random() for i in range(n)]for j in range(n)];print "B in main",B

M1 = [[0.0 for i in range(n)] for j in range(n)]
start_time = timeit.default_timer() #depends on platform ; can give process time or wall time ; OS dependant
M1= naive(A,B)
elapsed = timeit.default_timer() - start_time
print'time in sec:', round(elapsed,6)
#print "op matrix:",T4

