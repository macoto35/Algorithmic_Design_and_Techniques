
def greedyCalculator(n):
    numOfOperator = 0
    arr = []
    arr.append(n)

    while n > 1:
        numOfOperator += 1
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
        arr.append(n)

    print(len(arr))
    print(arr)

def dpCalculator(num, primitives):
    result = [99999] * (num + 1)
    result[0] = 0
    result[1] = 0

    for n in range(2, num + 1):
        minCnt = 0
        for p in primitives:
            if n >= p:
                if p == 1:
                    minCnt = result[n - 1] + 1
                else:
                    minCnt = result[n//p] + n % p + 1
            if result[n] > minCnt:
                result[n] = minCnt

    return result[num];

def dpCalculator_new(num, primitives):
    result = [99999] * (num + 1)
    result[0] = 0
    result[1] = 0

    for n in range(2, num + 1):
        minCnt = 99999
        for p in primitives:
            if n >= p:
                if p == 1:
                    minCnt = result[n - 1] + 1
                elif n % p == 0:
                    minCnt = result[n//p] + 1
            if result[n] > minCnt:
                result[n] = minCnt

    return result[num];

n = int(input())
# greedyCalculator(n)
print(dpCalculator(n, [1,2,3]))
print(dpCalculator_new(n, [1,2,3]))
