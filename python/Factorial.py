
def dpFactorial(n):
    result = [0 for i in range(0, n + 1)];
    result[1] = 1

    for i in range(2, n + 1):
        result[i] = result[i - 1] * i

    return result[n]

n = int(input())
print(dpFactorial(n))
