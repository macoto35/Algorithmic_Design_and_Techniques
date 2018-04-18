
from random import *

def ascAll(elem):
  return int(str(elem[0]) + str(elem[1]))


def ascB(elem):
  return elem[1]


def greedy(n, arr):
  res = []
  st = arr[0][0]
  ed = arr[0][1]
  #print("0:", st, ed)
  
  for i in range(1, n):
    a, b = arr[i][0], arr[i][1]
    #print(i,":", a, b)
    
    if ed < a:
      res.append([st, ed])
      st, ed = a, b
      #print("out of range: ", res, st, ed)
    else:
      if st < a:
        st = a
        #print("set st: ", st, a)
      if ed > b:
        ed = b
        #print("set ed: ", ed, b)
  res.append([st, ed])
 
  return res


def greedyFast(arr):
  res = []
  minRightPoint = 0
  
  while len(arr) > 0:
    res.append(arr[0][1])
    minRightPoint = arr[0][1]
    #print("minRightPoint: ", minRightPoint)

    arr = [ item for item in arr if item[0] > minRightPoint or item[1] < minRightPoint ]
    #print("arr:", arr)
  
  return res

'''
n = int(input())
arr = []
exec("arr.append([*map(int, input().split())]);" * n)

#arr.sort(key=ascAll)
#res = greedy(n, arr)
#print("greedy: ", len(res), "--->" , res)

arr.sort(key=ascB)
res1 = greedyFast(arr)
print("greedy fast:", len(res1), "--->" , res1)
'''

'''
N = int(input())
R = int(input())

while True:
  n = randint(1, N)
  arr = []
  for i in range(n):
    a, b = randint(0, R), randint(0, R)
    arr.append( [min(a, b), max(a, b)] )
  
  print("question: ", n, arr)
  arr.sort(key=ascAll)
  res = greedy(n, arr)
  print("greedy:", res)
  
  arr.sort(key=ascB)
  res1 = greedyFast(arr)
  print("greedy fast:", res1)
  
  if len(res) == len(res1):
    print(n, arr, res, res1, '-ok')
  else:
    print(n, arr, res, res1, '-fail')
    break
'''

file = open('sample/3_4_covering_segments.in', 'r')
n = int(file.readline())
arr = []
for i in range(n):
  arr.append([*map(int, file.readline().split())])

arr.sort(key=ascAll)
res = greedy(n, arr)

arr.sort(key=ascB)
res1 = greedyFast(arr)

print(len(res), len(res1))
