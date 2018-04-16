
'''
res1 = []
def naive(arr):
  for i in range(1, len(arr) + 1):
      pick(arr, 0, i)
  
def pick(arr, r, n):
  if r >= n:
    print(res1)
    return
  
  for i in range(len(arr)):
    res1.insert(r, arr.pop(i))
    pick(arr[i:], r + 1, n)
    arr.insert(i, res1.pop(r))
'''

def naive(arr):
  for i in range(1, len(arr) + 1):
    k = 0
    for j in range(0, len(arr), i):
      while k < len(arr) and k < j+i:
        print(arr[k], end = ' ')
        k += 1
      print(end = ' | ')
    print()


res2 = []
def greedy(arr):
  segment = []
  l = r = 0
  
  while len(arr) > 0:
    l = arr[0]
    r = l + 2
    
    while 1:
      if len(arr) > 0 and r >= arr[0]:
        segment.append(arr.pop(0))
      else:
        break
    res2.append(segment)
    segment = []
  print(res2)


res3 = []
def greedy2(arr):
  segment = []
  left = 0
  
  while left < len(arr):
    l = arr[left]
    r = l + 2
    
    while left < len(arr) and arr[left] <= r:
      segment.append(arr[left])
      left += 1
    
    res3.append(segment)
    segment = []
  
  print(res3)
    

arr = list(map(int, input().split()))
arr1 = list(arr)
#naive(arr)
greedy(arr)
greedy2(arr1)
