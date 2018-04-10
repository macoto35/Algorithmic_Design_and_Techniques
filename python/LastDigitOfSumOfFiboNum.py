
from random import *

def naive(n):
	if n <= 1:
		return n

	sum = 1
	prev = 0
	cur = 1
	
	for i in range(2, n + 1):
		prev, cur = cur, prev + cur
		sum += cur
	return sum % 10


def fast(n):
	if n <= 1:
		return n

	value = lastDigitFibo(n + 2)
	return (value - 1 if value > 0 else 9)


def lastDigitFibo(n):
	arr = []
	arr.append(0)
	arr.append(1)
	i = 2
	while 1:
		arr.append( (arr[i - 1] + arr[i - 2]) % 10 )
		if arr[i - 1] == 0 and arr[i] == 1:
			break
		else:
			i += 1

	return arr[ n % (i - 1) ]


n = int(input())
# print("naive: ", naive(n))
print("fast: ", fast(n))

'''
N = int(input())
while 1:
	n = randint(0, N)
	if naive(n) == fast(n):
		print(n, " - ok")
	else:
		print(n, " - fail")
		break
'''


