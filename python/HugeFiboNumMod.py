
from random import *

def naive(n, m):
	if n <= 1:
		return n

	previous = 0
	current = 1
	
	for i in range(2, n + 1):
		previous, current = current, previous + current

	return current % m

def fast(n, m):
	if n <= 1:
		return n
	
	arr = []
	arr.append(0)
	arr.append(1)
	i = 2
	while 1:
		arr.append( (arr[i - 1] + arr[i - 2]) % m )

		if arr[i - 1] == 0 and arr[i] == 1:
			break
		else:
			i += 1
	
	return arr[n % (i - 1)]
		

n, m = map(int, input().split())
# print(naive(n, m))
print(fast(n, m))

'''
N, M = map(int, input().split())

while 1:
	n = randint(1, N)
	m = randint(2, M)
	if naive(n, m) == fast(n, m):
		print(n, m, " - ok")
	else:
		print(n, m, " - fail")
		break
'''