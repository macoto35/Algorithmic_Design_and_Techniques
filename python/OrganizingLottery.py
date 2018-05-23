
from random import *

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

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr, st, ed):
    x = arr[st][0]
    m1 = m2 = st
    j = st + 1

    while j <= ed:
        if x > arr[j][0]:
            m1 += 1
            m2 += 1
            swap(arr, m2, j)
            swap(arr, m1, m2)
        elif x == arr[j][0]:
            m2 += 1
            swap(arr, m2, j)
            print(x, arr, m1, m2, j)--------------------------------------------------------------------------------
            if x == arr[m2 - 1] and arr[m2 - 1][1] == 'p':
                swap(arr, m2, m2 - 1)
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

def daqOrgLottery(segs, nums):
    arr = segs + nums
    quickSort(arr, 0, len(arr) - 1)
    print(arr)

    result = []
    count = []
    for i in range(0, len(arr)):
        p = arr[i]
        if p[1] == 'p':
            cnt = 0
            for j in range(0, i):
                if arr[j][1] != 'p':
                    if arr[j][1] == 'l':
                        cnt += 1
                    elif arr[j][0] == p[0] and arr[j][1] == 'r':
                        cnt += 0
                    else:
                        cnt += -1
                #print(p, arr[j], cnt)
            result.append([p[0], cnt if cnt  > 0 else 0])

    return result

'''
s,p = map(int, input().split())
segs = []
exec('l = [*map(int, input().split())]; segs.append([l[0], "l"]); segs.append([l[1], "r"]);' * s)
nums = [ [item, 'p'] for item in map(int, input().split()) ]
#print(*naiveOrgLottery(segs, nums))
print(daqOrgLottery(segs, nums))
'''


segs = [[6, 'l'], [10, 'r'], [5, 'l'], [7, 'r'], [2, 'l'], [10, 'r']]
nums = [[10, 'p'], [2, 'p'], [5, 'p'], [2, 'p'], [1, 'p']]
print(daqOrgLottery(segs, nums))
'''

S, P, Ki, Kj = map(int, input().split())
while True:
    s = randint(1, S)
    p = randint(1, P)
    segs1 = []
    segs2 = []
    for i in range(0, s):
        l = randint(Ki, Kj)
        r = randint(l, Kj)
        segs1.append([l, r])
        segs2.append([l, 'l'])
        segs2.append([r, 'r'])
    nums1 = []
    nums2 = []
    for i in range(0, p):
        val = randint(Ki, Kj)
        nums1.append(val)
        nums2.append([val, 'p'])

    print('segements: ', segs2, 'numbers: ', nums2)

    res1 = naiveOrgLottery(segs1, nums1)
    res2 = daqOrgLottery(segs2, nums2)
    print(res1, '|', res2, end = ' ')

    if sum(res1) == sum(r[1] for r in res2):
        print(' - pass!')
    else:
        print(' - fail!')
        break
'''