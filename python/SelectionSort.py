
def swap(arr, i, j):
  arr[i], arr[j] = arr[j], arr[i]

def selectionSort(arr):
  for i in range(len(arr)):
    minIdx = i
    for j in range(i, len(arr)):
      if arr[j] < arr[minIdx]:
        minIdx = j

    swap(arr, i, minIdx)
  
  return arr

arr = [8,4,2,5,2]
print(selectionSort(arr))