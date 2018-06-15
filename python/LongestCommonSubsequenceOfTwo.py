
def dpLCS(n, A, m, B):
    result = [[0 for i in range(0, m + 1)] for j in range(0, n + 1)];

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            insertion = result[i][j - 1]
            deletion = result[i - 1][j]
            mismatchOrMatch =  result[i - 1][j - 1] + 1 * (A[i - 1] == B[j - 1])
            result[i][j] = max(insertion, deletion, mismatchOrMatch)

    for r in result:
        print(r)

    return result[n][m]


n = int(input())
A = [*map(int, input().split())]
m = int(input())
B = [*map(int, input().split())]
print(dpLCS(n, A, m, B))
'''

file = open('../sample/5_4_lcs2.in')
n = int(file.readline())
A = [*map(int, file.readline().split())]
m = int(file.readline())
first.B = [*map(int, file.readline().split())]
print(dpLCS(n, A, m, first.B))
'''