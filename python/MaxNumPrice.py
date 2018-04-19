
def naive(n):
  k = 1
  sum = 0
  
  for i in range(1, n + 1):
    sum += i
    if sum > n:
      k = i - 1
      break

  return k

n = int(input())
k = naive(n)
print(k)
for i in range(1, k + 1):
  if i == k:
    print(i + n - (i*(i+1)//2), end = '')
  else:
    print(i, end = ' ')
