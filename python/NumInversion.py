
sum = 0

def merge(A, B):
  global sum
  C = []
  
  while len(A) > 0 and len(B) > 0:
    a = A[0]
    b = B[0]
    
    if a <= b:
      C.append(a)
      A.pop(0)
    else:
      C.append(b)
      B.pop(0)
      sum += len(A)

  C.extend( A if len(A) > 0 else B )
  return C

def numOfInversion(arr, st, ed):
  if st == ed:
    return [ arr[st] ]
  
  m = st + (ed - st) // 2
  A = numOfInversion(arr, st, m)
  B = numOfInversion(arr, m + 1, ed)
  return merge(A, B)

'''n = int(input())
arr = [*map(int, input().split())]
print(numOfInversion(arr, 0, n - 1))
print(sum)'''

file = open('sample/4_4_inversions.in', 'r')
n = int(file.readline())
arr = [*map(int, file.readline().split())]
print(numOfInversion(arr, 0, n - 1))
print(sum)
