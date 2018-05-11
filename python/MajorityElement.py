
from random import *

def naive(arr):
  count = 0
  cur = 0
  
  for i in range(len(arr)):
    count = 0
    cur = arr[i]
    for j in range(len(arr)):
      if arr[j] == cur:
        count += 1
    if count > len(arr)/2:
      return 1
  return 0


def greedy(arr):
  mid = len(arr)/2
  count = 0
  cur = 0
  idx = 0
  
  while len(arr) > 0:
    count = 0
    idx = 0
    cur = arr[0]
    while len(arr) > idx:
      if cur == arr[idx]:
        count += 1
        arr.pop(idx)
      else:
        idx += 1
    if count > mid:
      return 1
  return 0


def scan(arr, size):
  elemt = -1
  cnt = 0
  
  while len(arr) > 0:
    x = arr[0]
    i = 0
    cnt = 0
    while len(arr) > i and len(arr) > 0:
      if x == arr[i]:
        arr.pop(i)
        cnt += 1
      else:
        i += 1
    if cnt > size // 2:
      elemt = x
      break

  return elemt

def findMajority(arr, st, ed, a, b):
  if a == b:
    return a
  else:
    return scan(arr[st:ed + 1], ed - st + 1)

def divideAndConquer(arr, st, ed):
  if st == ed:
    return arr[st]
  
  m = st + (ed - st) // 2
  
  a = divideAndConquer(arr, st, m)
  b = divideAndConquer(arr, m + 1, ed)
  return findMajority(arr, st, ed, a, b)

'''
arr = [2,2,3,7,7]
arr1 = [1,2,3,1,1]
print(naive(arr))
print(greedy(arr1))
print(divideAndConquer(arr, 0, len(arr1) - 1))
'''

'''
N, I = input().split()
while True:
  n = randint(1, int(N))
  arr = []
  for i in range(n):
    arr.append(randint(0, int(I)))
  arr1 = arr[0:len(arr)]
  
  print(arr, arr1, end = ' ')
  r1 = greedy(arr)
  r2 = 1 if divideAndConquer(arr1, 0, len(arr1) - 1) > -1 else 0
  
  if (r1 == r2):
    print(' - pass!')
  else:
    print(' - fail!')
    break
'''

file = open('sample/4_2_majority_element.in', 'r')
n = file.readline()
arr = [*map(int, file.readline().split())]

#print(greedy(arr))
print(divideAndConquer(arr, 0, len(arr) - 1))

