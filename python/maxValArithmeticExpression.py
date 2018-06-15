
def parentheses(num, oper):
    n = len(num)
    m = [[0 for i in range(0, n)] for j in range(0, n)]
    M = [[0 for i in range(0, n)] for j in range(0, n)]

    for i in range(0, n):
        m[i][i] = M[i][i] = int(num[i])

    for s in range(1, n):
        for i in range(0, n - s):
            j = i + s
            m[i][j], M[i][j] = minAndMax(m, M, oper, i, j)

    return M[0][n - 1]

def minAndMax(m, M, oper, i, j):
    minVal = 99999
    maxVal = -99999
    for k in range(i, j):
        a = eval( str(M[i][k]) + oper[k] + str(M[k+1][j]) )
        b = eval( str(M[i][k]) + oper[k] + str(m[k+1][j]) )
        c = eval( str(m[i][k]) + oper[k] + str(M[k+1][j]) )
        d = eval( str(m[i][k]) + oper[k] + str(m[k+1][j]) )
        minVal = min(minVal, a, b, c, d)
        maxVal = max(maxVal, a, b, c, d)
    return [minVal, maxVal]

arr = list(input())
print(parentheses(arr[0::2], arr[1::2]))
