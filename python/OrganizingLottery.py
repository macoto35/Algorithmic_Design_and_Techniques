'''
def naiveOrgLottery(segs, nums):
  result = []
  sum = 0

  for n in nums:
    sum = 0
    for s in segs:
      if (s[0] <= n and s[1] >= n):
        sum += 1
    result.append(sum)

  return result
print(*naiveOrgLottery(segs, nums))
'''

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr, st, ed):
    x = arr[st][0]
    m1 = m2 = st
    j = st + 1

    print(arr, st, ed, x, m1, m2, j)
    while j <= ed:
        print(arr, j,'/',ed, arr[j][0])
        if x > arr[j][0]:
            m1 += 1
            m2 += 1
            print('small: ', m1, m2, j)
            swap(arr, m2, j)
            swap(arr, m1, m2)
        if x == arr[j][0]:
            m2 += 1
            print('same: ',m2, j)
            swap(arr, m2, j)
        j += 1

    swap(arr, st, m1)
    return [m1, m2]

def findPivot(arr, st, ed):
    m = st + (ed - st) // 2
    i = arr[st][0]
    j = arr[m][0]
    k = arr[ed][0]
    pivot = st

    if i >= j and i >= k:
        pivot = m if j >= k else ed
    if j >= i and j >= k:
        pivot = st if i >= k else ed
    if k >= i and k >= j:
        pivot = st if i >= j else m

    swap(arr, st, pivot)

def quickSort(arr, st, ed):
    while st <= ed:
        findPivot(arr, st, ed)
        m1, m2 = partition(arr, st, ed)
        if (m1 - st) <= (ed - m2):
            quickSort(arr, st, m1 - 1)
            st = m2 + 1
        else:
            quickSort(arr, m2 + 1, ed)
            ed = m1 - 1

'''
s,p = map(int, input().split())
segs = []
exec('segs.append([*map(int, input().split())]); ' * s)
nums = [*map(int, input().split())]
'''

segs = [[2,7],[2,2],[1,3]]
quickSort(segs, 0, len(segs) - 1)
print(segs)
