
maxRev = []
tmpA = []
tmpB = []
def naive(r, n, a, b):

  if r == n:
    rev = 0
    for i in tmpA:
      for j in tmpB:
        rev += i * j

    maxRev.append(rev);
    
    print("tmpA:", tmpA)
    print("tmpB", tmpB)
    print("maxRev", maxRev)
    return
  
  for i in range(len(a)):
    print("i/r", i, "/", r)
    tmpA.insert(r, a.pop(i))
    for j in range(n):
      print("j/r", j, "/", r)
      tmpB.insert(r, b.pop(j))
      naive(r + 1, n, a, b)
      print("--j/r", j, "/", r)
      b.insert(j, tmpB.pop(r))
    print("--i/r", i, "/", r)
    a.insert(i, tmpA.pop(r))

def greedy(n, a, b):
  sum = 0
  for i in range(n):
    sum += a[i]*b[i]
  return sum

n = int(input())
a = [*map(int, input().split())]
b = [*map(int, input().split())]

naive(0, n, a, b)
print(maxRev)

'''
a.sort(reverse=True)
b.sort(reverse=True)
print(greedy(n, a, b))
'''