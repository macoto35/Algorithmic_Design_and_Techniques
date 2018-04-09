
from random import * 

def naive(a, b):
	for l in range(1, a * b + 1):
		if l % a == 0 and l % b == 0:
			return l
	return a * b

def fast(a, b):
	return a * b // GCD(a, b)

def GCD(a, b):
	if b == 0:
		return a
	return GCD(b, a % b)

a, b = map(int, input().split())
# print(naive(a, b))
print(fast(a, b))

'''
n = int(input())

while 1:
	a = randint(1, n)
	b = randint(1, n)
	
	if naive(a, b) == fast(a, b):
		print(a, b, " - ok")
	else:
		print(a, b, " - fail")
		break
'''