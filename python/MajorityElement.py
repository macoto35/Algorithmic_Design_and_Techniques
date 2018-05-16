
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
      return cur
  return -1


def scan(arr, st, m, ed, a, b):
  if a[0] != -1:
    for i in range(m + 1, ed + 1):
      if a[0] == arr[i]:
        a[1] += 1

  if b[0] != -1:
    for i in range(st, m + 1):
      if b[0] == arr[i]:
        b[1] += 1

  m = (ed - st + 1) //2

  if a[1] > m:
    return a
  elif b[1] > m:
    return b
  else:
    return [-1, 0]

def findMajority(arr, st, m, ed, a, b):
  if a[0] == b[0]:
    return [a[0], a[1]+b[1]]
  else:
    return scan(arr, st, m, ed, a, b)

def divideAndConquer(arr, st, ed):
  if st == ed:
    return [arr[st], 1]
  
  m = st + (ed - st) // 2
  
  a = divideAndConquer(arr, st, m)
  b = divideAndConquer(arr, m + 1, ed)
  return findMajority(arr, st, m, ed, a, b)


def merge(A, B):
  if len(A[0]) > 0 and len(B[0]) > 0 and A[0][0] == B[0][0]:
    A[0] += B[0]
    B[0] = []
  else:
    i = 0
    while len(B[1]) > i :
      if len(A[0]) > 0 and B[1][i] == A[0][0]:
        A[0].append(B[1].pop(i))
      else:
        i += 1

    i = 0
    while len(A[1]) > i:
      if len(B[0]) > 0 and A[1][i] == B[0][0]:
        B[0].append(A[1].pop(i))
      else:
        i += 1

  majorityCnt = len(A[0]+A[1]+B[0]+B[1]) // 2

  if len(A[0]) > majorityCnt:
    A[1] += B[0] + B[1]
    return A
  elif len(B[0]) > majorityCnt:
    B[1] += A[0] + A[1]
    return B
  else:
    return [[], A[0]+A[1]+B[0]+B[1]]

def divideAndConquerNew(arr, st, ed):
  if st == ed:
    return [[ arr[st] ], []];

  m = st + (ed - st) // 2

  A = divideAndConquerNew(arr, st, m)
  B = divideAndConquerNew(arr, m + 1, ed)

  return merge(A, B)


def mooreVotingAlgo(arr):
    majorityElemt = arr[0]
    cnt = 1

    # find candidate
    for i in arr[1:]:
        if majorityElemt == i:
            cnt += 1
        else:
            cnt -= 1

        if cnt == 0:
            majorityElemt = i
            cnt = 1

    # check the candidate is majority elemt
    cnt = 0
    for i in arr:
        if majorityElemt == i:
            cnt += 1

    if cnt > len(arr) // 2:
        return majorityElemt
    else:
        return -1

'''
arr = [2,2,3,2,7]
arr1 = [1,2,3,1,1]
#print(naive(arr))
#print(greedy(arr1))
#print(divideAndConquer(arr, 0, len(arr) - 1))
#print(divideAndConquerNew(arr, 0, len(arr) - 1))
#print(mooreVotingAlgo(arr))
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
  r2 = 1 if len(divideAndConquerNew(arr1, 0, len(arr1) - 1)[0]) > 0 else 0
  
  if (r1 == r2):
    print(' - pass!')
  else:
    print(' - fail!')
    break
'''


file = open('../sample/4_2_majority_element.in', 'r')
n = file.readline()
arr = [*map(int, file.readline().split())]

#print(greedy(arr))
#print(divideAndConquer(arr, 0, len(arr) - 1))
#print(divideAndConquerNew(arr, 0, len(arr) - 1)[0][0])
print(mooreVotingAlgo(arr))
