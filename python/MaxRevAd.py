
def greedy(n, a, b):
  sum = 0
  for i in range(n):
    sum += a[i]*b[i]
  return sum


n = int(input())
a = [*map(int, input().split())]
b = [*map(int, input().split())]

a.sort(reverse=True)
b.sort(reverse=True)
print(greedy(n, a, b))

'''
file = open('sample/3_3_dot_product20180216.in', 'r')
n = int(file.readline())
a = [*map(int, file.readline().split())]
b = [*map(int, file.readline().split())]
a.sort(reverse=True)
b.sort(reverse=True)
print(greedy(n, a, b))
'''