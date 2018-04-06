import time

def naiveSol(n):
	if n <= 1:
		return n
	else:
		return naiveSol(n-1) + naiveSol(n-2)

def fastSol(n):
    arr = []
    arr.append(0)
    arr.append(1)
    
    for i in range(2, n + 1):
    	arr.append( arr[i - 1] + arr[i - 2] )

    return arr[n]

#n = int(input())

result = 1
n = 0
while result and n <= 45:
	#startTime = time.time()
	a = naiveSol(n)
	b = fastSol(n)
	if a == b:
		print(n, " - ok")
		n += 1
	else:
		printprint(n, " - fail")
		result = 0
	#print("elapsed time: ", time.time() - startTime)
