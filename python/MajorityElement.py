
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

def divideAndConquer(arr, st, ed):
  print('enter: ',st,ed)
  if st == ed:
    print('return=====', arr[st])
    return arr[st]
  
  mid = st + (ed - st) // 2
  
  a = divideAndConquer(arr, st, mid)
  b = divideAndConquer(arr, mid + 1, ed)
  
  print('next-------- ', a, b)

arr = [1,2,3,1,1]
arr1 = [1,2,3,1,1]
#print(naive(arr))
#print(greedy(arr1))
print(divideAndConquer(arr, 0, len(arr)-1))
