
def dpMaxAmountGold(W, n, golds):
    result = [[0 for i in range(0, W + 1)] for j in range(0, n + 1)]

    for i in range(1, n + 1):
        value = 0
        for w in range(0, W + 1):
            result[i][w] = result[i - 1][w]
            if golds[i - 1] <= w:
                value = result[i - 1][w - golds[i - 1]] + golds[i - 1]

                if value > result[i][w]:
                    result[i][w] = value

    print(result)
    return result[n][W]

'''
W, n = map(int, input().split())
golds = [*map(int, input().split())]
print(dpMaxAmountGold(W, n, golds))
'''

file = open('../sample/6_1_knapsack.in')
W, n = map(int, file.readline().split())
golds = [*map(int, file.readline().split())]
print(dpMaxAmountGold(W, n, golds))
