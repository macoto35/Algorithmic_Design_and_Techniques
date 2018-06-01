
def dpKnapSackWithoutRepetitions(W, A):
    # find knapsack max target value
    result = [[0 for i in range(0, W + 1)] for j in range(0, len(A) + 1)];

    for i in range(1, len(A) + 1):
        val = 0
        for w in range(1, W + 1):
            result[i][w] = result[i - 1][w];
            if A[i - 1] <= w:
                val = result[i - 1][w - A[i - 1]] + A[i - 1]
                if result[i][w] < val:
                    result[i][w] = val

    returnVal = result[len(A)][W]

    # find components and remove from values
    used = []
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

    if len(used) > 0:
        for i in used:
            A.pop(i)

    return returnVal

def dpPartitioningSouvenirs(n, values, totalSum):
    if totalSum % 3 != 0:
        return 0

    W = totalSum // 3

    W1 = dpKnapSackWithoutRepetitions(W, values)
    W2 = dpKnapSackWithoutRepetitions(W, values)
    W3 = sum(values)

    if W == W1 and W == W2 and W == W3:
        return 1
    else:
        return 0

'''
n = int(input())
values = [*map(int, input().split())]
print(dpPartitioningSouvenirs(n, values, sum(values)))
'''

file = open('../sample/6_2_souvenirs.in')
while True:
    line1 = file.readline()
    line2 = file.readline()
    line3 =  file.readline()
    if not line2:
        break
    else:
        n = int(line1)
        values = [*map(int, line2.split())]
        print(dpPartitioningSouvenirs(n, values, sum(values)), end='')