
def memorySol(n):
	arr = []
	arr.append(0)
	arr.append(1)
	
	for i in range(2, n + 1):
		arr.append((arr[i - 1] + arr[i - 2]) % 10)
	
	return arr[n]

def alternativeSol(n):
	if n <= 1:
		return n

	previous = 0
	current = 1
	
	for i in range(2, n + 1):
		previous, current = current, (previous + current) % 10

	return current

n = int(input())
print(alternativeSol(n))

'''
for n in range(0, 10000001):
	a = memorySol(n)
	b = alternativeSol(n)
	if a == b:
		print(n, " - ok")
	else:
		print(n, " - fail", a, "/", b)
		break
'''