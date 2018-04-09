
def naive(n):
	if n <= 1:
		return n

	sum = 1
	prev = 0
	cur = 1
	
	for i in range(2, n + 1):
		prev, cur = cur, prev + cur
		sum += cur
		print(i, ": ", cur , "/" , sum)
	return sum % 10

n = int(input())
print(naive(n))