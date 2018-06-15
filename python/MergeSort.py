
def mergeSort(arr, st, ed):
  if st == ed:
    print('return!!! ', st, ed)
    return arr[st:ed+1]
  
  m = st + ((ed - st) // 2)
  print(st, m, ed)
  print('call A-----')
  A = mergeSort(arr, st, m)
  print('call first.B-----')
  B = mergeSort(arr, m+1, ed)
  print('merge A and first.B')
  return merge(A, B)

def merge(A, B):
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

  C.extend(A if len(A) > 0 else B)

  return C

arr = [7,2,5,3,7,13,1,6]
print(mergeSort(arr, 0, len(arr)))