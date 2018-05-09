
from random import *

def swap(arr, i, j):
  arr[i], arr[j] = arr[j], arr[i]

def partition(arr, l, r):
  x = arr[l]
  j = l
  
  for i in range(l + 1, r):
    if arr[i] <= x:
      j += 1
      swap(arr, i, j)

  swap(arr, l, j)
  return j


def quickSort(arr, l, r):
  if l >= r:
    return
  
  m = partition(arr, l, r)
  print('call first: ', l, m - 1)
  quickSort(arr, l, m - 1)
  print('call second: ', m + 1, r)
  quickSort(arr, m + 1, r)


def randomiseQuickSort(arr , l, r):
  if l >= r:
    return
  
  k = randint(l, r - 1)
  swap(arr, l, k)
  
  m = partition(arr, l, r)
  randomiseQuickSort(arr , l, m - 1)
  randomiseQuickSort(arr , m + 1, r)


def partitionEqualElement(arr, l, r):
  x = arr[l]
  m1 = m2 = l
  
  for i in range(l + 1, r):
    if arr[i] < x:
      if m1 != m2:
        swap(arr, m2, m2+1)  
      m2 += 1
      m1 += 1
      swap(arr, m1, i)
    elif arr[i] == x:
      m2 += 1
      swap(arr, m2, i)
  swap(arr, m1, l)
  return [m1, m2]


def randomiseQuickSortEqualElement(arr, l, r):
  if l >= r:
    return
  
  k = randint(l, r - 1)
  swap(arr, k, l)
  
  m1, m2 = map(int, partitionEqualElement(arr, l, r))
  
  randomiseQuickSortEqualElement(arr, l, m1 - 1)
  randomiseQuickSortEqualElement(arr, m2 + 1, r)


def searchMed(arr, l, r):  
  val = sorted([ arr[l], arr[l + (r - l) // 2], arr[r]])[1]
  swap(arr, arr.index(val), l)


def improveRandomiseQuickSortEqualElement(arr, l, r):
  if l >= r:
    return
  
  searchMed(arr, l, r - 1)
  
  m1, m2 = map(int, partitionEqualElement(arr, l, r))
  
  randomiseQuickSortEqualElement(arr, l, m1 - 1)
  randomiseQuickSortEqualElement(arr, m2 + 1, r)


def quickSortLessMemory(arr, l, r):
  while l < r:
    m = partition(arr, l, r)
    print('call first: ', l, m - 1)
    quickSortLessMemory(arr, l, m - 1);
    l = m + 1


def quickSortLessMemory2(arr, l, r):
  while l < r:
    m = partition(arr, l, r)
    
    if (m - l) < (r - m):
      print('call first: ', l, m - 1)
      quickSortLessMemory2(arr, l, m - 1)
      l = m + 1
    else:
      print('call second: ', m + 1, r)
      quickSortLessMemory2(arr, m + 1, r)
      r = m - 1


arr = [1,4,2,8,7,7,9,11]
# quickSort(arr, 0, len(arr))
# randomiseQuickSort(arr , 0, len(arr))
# randomiseQuickSortEqualElement(arr, 0, len(arr))
improveRandomiseQuickSortEqualElement(arr, 0, len(arr))
print(arr)

# arr1 = [1,4,2,8,7,7,9,11]
# quickSortLessMemory(arr1, 0, len(arr))
# quickSortLessMemory2(arr1, 0, len(arr))
# print(arr1)

