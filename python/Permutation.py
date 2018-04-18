
# recursive + array
'''
res = []
def perm(arr, r, n):
  if r == n:
    print(res)
    return
    
  for i in range(len(arr)):
    res.insert(r, arr.pop(i))
    perm(arr, r + 1, n)
    arr.insert(i, res.pop(r))

arr = [1,2,3]
for i in range(1, len(arr) + 1):
  perm(arr, 0, i)
'''

# recursive + swap
def swap(arr, i, j):
  arr[i], arr[j] = arr[j], arr[i]

res = []
def permSwap(arr, depth, r, n):
  print('enter: ', arr, depth, r, n)
  if depth == r:
    print('------------------', res)
    return
    
  for i in range(depth, n):
    swap(arr, depth, i)
    print('swap: ', arr, depth, r, n, i)
    res.insert(depth, arr[depth])
    print('res: ', res)
    permSwap(arr, depth+1, r, n)
    swap(arr, depth, i)
    res.pop(depth)
    print('swap rollback: ', arr, depth, r, n, i)
  
arr = [1,2,3]
permSwap(arr, 0, 2, len(arr))
