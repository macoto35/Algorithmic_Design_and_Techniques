
from random import *

def dpLCS3D(n, A, m, B, l, C):
    result = [[[0 for k in range(0, l + 1)] for j in range(0, m + 1)] for i in range(0, n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l + 1):
                a = result[i][j][k - 1]
                b = result[i][j - 1][k]
                c = result[i - 1][j][k]
                d = result[i][j - 1][k - 1]
                e = result[i - 1][j][k - 1]
                f = result[i - 1][j - 1][k]
                g = result[i - 1][j - 1][k - 1] + (1 if A[i - 1] == B[j - 1] and B[j - 1] == C[k - 1] else 0)
                result[i][j][k] = max(a,b,c,d,e,f,g)

    #print(result)
    return result[n][m][l]

def dpLCS2D(n, A, m, B):
    result = [[0 for i in range(0, m + 1)] for j in range(0, n + 1)];

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            insertion = result[i][j - 1]
            deletion = result[i - 1][j]
            mismatchOrMatch =  result[i - 1][j - 1] + 1 * (A[i - 1] == B[j - 1])
            result[i][j] = max(insertion, deletion, mismatchOrMatch)

    #for r in result:
    #    print(r)

    return result[n][m]

def dpLCS3Times(n, A, m, B, l, C):
    return min(dpLCS2D(n, A, m, B), dpLCS2D(m, B, l, C), dpLCS2D(n, A, l, C))

'''
arr = []
exec('arr.append( int(input()) ); arr.append( [*map(int, input().split())] );' * 3)
print(dpLCS3D(*arr))
print(dpLCS3Times(*arr))
'''

'''
size, st, ed = map(int, input().split())

while True:
    arr = []

    for i in range(0, 3):
        n = randint(1, size)
        A = [randint(st, ed) for j in range(0, n)]
        arr.append(n)
        arr.append(A)
    print(arr)

    r1 = dpLCS3D(*arr)
    r2 = dpLCS3Times(*arr)
    print(r1, r2, end=' ')

    if r1 == r2:
        print(' - success!')
    else:
        print(' - fail!')
        break
'''

file = open('../sample/5_5_lcs3.in')
arr = []
exec('arr.append( int(file.readline()) ); arr.append( [*map(int, file.readline().split())] );' * 3)
print(dpLCS3D(*arr))