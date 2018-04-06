from random import *

def naive(a, b):
	if b == 0:
		return a

	currentGcd = 1
	
	for d in range(2, min(a, b) + 1):
		if a % d == 0 and b % d == 0:
			currentGcd = d

	return currentGcd

def euclidean(a, b):
	if b == 0:
		return a

	return euclidean(b, a % b)

a, b = map(int, input().split())
# print(naive(a, b) if a > b else naive(b, a))
print(euclidean(a, b) if a > b else euclidean(b, a))

'''
n = int(input())

while 1:
	a = randint(1, n)
	b = randint(1, n)
	print(a, b)
	
	r1 = naive(a, b) if a > b else naive(b, a)
	r2 = euclidean(a, b) if a > b else euclidean(b, a)
	
	if r1 == r2:
		print(" - ok")
	else:
		print(" - fail")
		break
'''