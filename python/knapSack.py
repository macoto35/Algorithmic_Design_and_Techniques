
def dpKnapSackWithRepetitions(W, A):
    value = [0] * (W + 1)

    for w in range (1, W + 1):
        val = 0
        for a in A:
            if w >= a[0]:
                val = value[w - a[0]] + a[1]
            if value[w] < val:
                value[w] = val

    for v in value:
        print(v, end = ' ')

    return value[W]

W = 10
A = [[6, 30], [3, 14], [4, 16], [2, 9]]
dpKnapSackWithRepetitions(W, A)