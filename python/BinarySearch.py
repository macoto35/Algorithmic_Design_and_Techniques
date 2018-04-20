
from random import *

def linearSearch(arr, low, high, key):
  '''if low > high:
    return -1
  if key == arr[low]:
    return low
  
  return linearSearch(arr, low + 1, high, key)'''
  for i in range(low, high + 1):
    if key == arr[i]:
      return i
  return -1
    
  
def binarySearch(arr, low, high, key):
  if low > high:
    return -1
  
  mid = low + (high - low) // 2
  
  if key == arr[mid]:
    return mid;
  elif key < arr[mid]:
    return binarySearch(arr, low, mid - 1, key)
  else:
    return binarySearch(arr, mid + 1, high, key)

'''
# single input check
n, *A = map(int, input().split())
k, *B = map(int, input().split())

for b in B:
  print(linearSearch(A, 0, n - 1, b), end = ' ')
print()
for b in B:
  print(binarySearch(A, 0, n - 1, b), end = ' ')
'''

'''
# random number check
N, I = map(int, input().split())

while True:
  n = randint(1, N)
  A = []
  while len(A) < n:
    for i in range(n):
      A.append(randint(1, I))
    A = list(set(A))
  A.sort()
  
  k = randint(1, N)
  B = []
  for i in range(k):
    B.append(randint(1, I))
  B.sort()
  
  print(n, A, k, B);
  
  res1 = [];
  for b in B:
    res1.append(linearSearch(A, 0, n - 1, b))
    
  res2 = [];
  for b in B:
    res2.append(binarySearch(A, 0, n - 1, b))
  
  if res1 == res2:
    print(res1, res2, ' - ok')
  else:
    print(res1, res2, ' - fail')
    break
'''

# file check
file = open('sample/4_1_binary_search.in', 'r')
n, *A = map(int, file.readline().split())
k, *B = map(int, file.readline().split())

res2 = []
for b in B:
  res2.append(binarySearch(A, 0, n - 1, b))
print(len([x for x in res2 if x > -1]))
