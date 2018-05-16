
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

s,p = map(int, input().split())
segs = []
exec('segs.append([*map(int, input().split())]); ' * s)
nums = [*map(int, input().split())]
#print(*naiveOrgLottery(segs, nums))
