
from random import *

def naive(m, n):
    
    sum = 0
    current = 0
    next = 1

    for i in range(n + 1):
        if i >= m:
            sum += current
        current, next = next, (current + next)

    return sum % 10


def fast(m, n):
    if n <= 1:
        return n

    a = getFibo(n + 2)
    b = getFibo(m + 1)
    
    return a - b if a >= b else a - b + 10

def setFibo():
    arr = []
    arr.append(0)
    arr.append(1)
    i = 2

    while(1):
        arr.append( (arr[i - 1] + arr[i - 2]) % 10 )
        if arr[i - 1] == 0 and arr[i] == 1:
            break
        else:
            i += 1
    return arr[:i - 1]

def getFibo(v):
    a = arr[ v % len(arr) ]
    return 9 if a == 0 else a - 1

arr = setFibo()

m, n = map(int, input().split())
# print("naive: ", naive(m, n))
print("fast: ", fast(m, n))

'''
N = int(input())

while 1:
	a = randint(0, N)
	b = randint(0, N)
	m = min(a, b)
	n = max(a, b)
	if naive(m, n) == fast(m, n):
		print(m, n, " - ok")
	else:
		print(m, n, " - fail")
		break
'''