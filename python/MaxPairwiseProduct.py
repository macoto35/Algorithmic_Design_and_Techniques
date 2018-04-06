'''
n = int(input())
a = list(map(int, input().split()))

product = 0
for i in range(n):
    for j in range(i+1, n):
        product = max(product, a[i] * a[j])
print(product)


n = int(input())
a = list(map(int, input().split()))
a.sort()
print(a[n - 1] * a[n - 2])
'''

from random import *

def naive(n, a):
    product = 0
    for i in range(n):
        for j in range(i+1, n):
            product = max(product, a[i] * a[j])
    return product

def fast(n, a):
    a.sort()
    return a[n - 1] * a[n - 2]

N, M = map(int, input().split())

while 1:
    n = randint(2, N)
    a = []
    for i in range(n):
        a.append( randint(0, M) )
    print(a)
    
    result1 = naive(n, a)
    result2 = fast(n, a)
    
    if result1 == result2:
        print("ok")
    else:
        print("wrong answer : ", result1, result2)
