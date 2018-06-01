
def dpKnapSackWithRepetitions(W, A):
    value = [0] * (W + 1)

    for w in range (1, W + 1):
        val = 0
        for a in A:
            if w >= a[0]:
                val = value[w - a[0]] + a[1]
            if value[w] < val:
                value[w] = val

    #for v in value:
    #    print(v, end = ' ')

    return value[W]

def dpKnapSackWithoutRepetitions(W, A):
    result = [[0 for i in range(0, W + 1)] for j in range(0, len(A) + 1)];

    for i in range(1, len(A) + 1):
        val = 0
        for w in range(1, W + 1):
            result[i][w] = result[i - 1][w];
            weight = A[i - 1][0];
            value = A[i - 1][1];
            if weight <= w:
                val = result[i - 1][w - weight] + value
                if result[i][w] < val:
                    result[i][w] = val

    #print(result)
    '''used = []
    i = len(A)
    w = W
    while i != 0 and w != 0:
        curVal = result[i][w]
        preValNotIn = result[i - 1][w]

        if curVal != preValNotIn:
            w = w - A[i - 1]
            i = i - 1
            used.append(i)
        else:
            i = i - 1
    print(used)'''


    return result[len(A)][W]

W = 10
A = [[6, 30], [3, 14], [4, 16], [2, 9]]
#print(dpKnapSackWithRepetitions(W, A))
print(dpKnapSackWithoutRepetitions(W, A))
