
def countSort(arr, M):
  count = [0] * M
  for i in range(len(arr)):
    count[arr[i]] += 1
  
  pos = [0] * M
  for j in range(1, M):
    pos[j] = pos[j - 1] + count[j - 1]
  
  ret = [0] * len(arr)
  for i in range(len(arr)):
    ret[pos[arr[i]]] = arr[i]
    pos[arr[i]] += 1
    
  return ret

arr = [2,3,2,1,3,2,2,3,2,2,2,1]
print(countSort(arr, 4))