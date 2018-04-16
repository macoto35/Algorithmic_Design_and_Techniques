
from random import *

#o((n+1)^3)
def naive(m):
  arr = []

  for i in range(0, m + 1):
    for j in range(0, m + 1):
      for k in range(0, m + 1):
        if i * 1 + j * 5 + k * 10 == m:
          arr.append(i + j + k)
  return min(arr)

#O(n)    
def greedy(m):
  arr = [10, 5, 1]
  remain = m;
  cnt = 0;
  
  for i in arr:
      cnt += remain // i
      remain = remain % i
  
  return cnt

'''
m = int(input())
print(naive(m))
print(greedy(m))
'''

M = int(input())
while 1:
  m = randint(0, M)
  if naive(m) == greedy(m):
    print(m, ' - ok')
  else:
    print(m, ' - fail')
    break
