
from random import *

def dpEditDistance(s1, s2, M, N):
    result = []
    for m in range(0, M + 1):
        result.append([(m + n) * (m == 0 or n == 0) for n in range(0, N + 1) ])

    for i in range(1, M + 1):
        for j in range(1, N + 1):
            insertion = result[i][j - 1] + 1
            deletion = result[i - 1][j] + 1
            matchOrMismatch = result[i - 1][j - 1] + 1 * (s1[i - 1 : i] != s2[j - 1 : j])

            result[i][j] = min(insertion, deletion,matchOrMismatch)

    for r in result:
        print(r)

    return result[M][N]

'''
s1, s2 = input(), input()
print(dpEditDistance(s1, s2, len(s1), len(s2)))
'''

'''
while True:
    len1 = randint(1,100)
    len2 = randint(1,100)
    s1 = ''.join([chr(randint(97,122)) for i in range(0, len1)])
    s2 = ''.join([chr(randint(97,122)) for j in range(0, len2)])

    print(s1)
    print(s2)
    print(dpEditDistance(s1, s2, len(s1), len(s2)))
    print('-----------------------------------------------')
'''


f = open('../sample/5_3_edit_distance.in')
s1 = f.readline()
s2 = f.readline()
print(dpEditDistance(s1, s2, len(s1), len(s2)))
