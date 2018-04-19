
from random import *

res = []
def allCaseMemory(arr, depth, n):
  if depth == n:
    print('memory: ', res)
    return
    
  for i in range(len(arr)):
    res.insert(depth, arr.pop(i))
    allCaseMemory(arr, depth + 1, n)
    arr.insert(i, res.pop(depth))


def swap(arr, i, j):
  arr[i], arr[j] = arr[j], arr[i]

result = []
res1 = []
def allCaseSwap(arr, depth, n, len):
  if depth == n:
    result.append(''.join(map(str, res1)))
    return
  
  for i in range(depth, len):
    swap(arr, depth, i)
    res1.insert(depth, arr[depth])
    allCaseSwap(arr, depth + 1, n, len)
    swap(arr, depth, i)
    res1.pop()


def comp(elem):
  return int(elem)


def compOne(elem):
  n = str(elem)
  return n.ljust(4, n[-1:])

def compTwo(a, b):
  A, B = str(a), str(b)
  return int(A+B) >= int(B+A)

def largestNum(arr):
  answer = ''
  
  while len(arr) > 0:
    maxDigit = 0
    idx = 0
    for i in range(len(arr)):
      if compTwo(arr[i], maxDigit):
        maxDigit = arr[i]
        idx = i
        #print("maxDigit:", maxDigit)
    #print("maxDigit / i: ", maxDigit, i)
    answer += str(maxDigit)
    arr.pop(idx)
    #print("arr: ", arr)
  
  return answer

'''
n = int(input())
arr = [*map(int, input().split())]

# naive algorithm
allCaseMemory(arr, 0, n)
allCaseSwap(arr, 0, n, len(arr))
result.sort(key = comp, reverse = True)
print(result[0])

# greedy algorithm
#arr.sort(key = compOne, reverse = True)
#for item in arr:
#  print(item, end = '')
print(largestNum(arr))
'''

'''
N, I = map(int, input().split())
while True:
  print('start----------------------------')
  n = randint(1, N)
  arr = []
  for i in range(n):
    arr.append(randint(1, I))

  print(n, arr, end = '     ')
  
  #allCaseSwap(arr, 0, n, len(arr))
  #result.sort(key = comp, reverse = True)
  #r1 = result[0]
  #result = []
  #res1 = []
  arr.sort(key = compOne, reverse = True)
  r1 = ''.join(map(str, arr))
  
  r2 = largestNum(arr)
  
  if r1 == r2:
    print(r1, r2, ' - ok')
  else:
    print(r1, r2, ' - fail')
    break
'''

file = open('sample/3_6_largest_number.in', 'r')
n = int(file.readline())
arr = [*map(int, file.readline().split())]
print(largestNum(arr))
