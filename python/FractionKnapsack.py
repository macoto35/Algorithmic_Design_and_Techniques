
import copy
from random import *

def bestItem(items):
  maxUnitPrice = idx = val = 0
  
  for i in range(len(items)):
    if items[i][1] > 0:
    	val = items[i][0] / items[i][1]
    	if maxUnitPrice < val:
      		maxUnitPrice = val
      		idx = i
  return idx


def greedy(W, items):
  maxValue = idx = 0
  
  for i in range(len(items)):
    if W == 0:
      break;
    
    idx = bestItem(items)
    a = min(items[idx][1], W)
    maxValue += a * items[idx][0] / items[idx][1]
    items[idx][1] -= a
    W -= a
  
  return maxValue


def unitCost(elem):
  return elem[0] / elem[1]


def greedyFast(W, items):
  maxValue = 0
  
  for i in range(len(items)):
    if W == 0:
      break
    
    a = min(items[i][1], W)
    maxValue += a * items[i][0] / items[i][1]
    W -= a

  return maxValue

'''
n, W = map(int, input().split())
items = []
exec("items.append([*map(int, input().split())]);" * n)

items1 = copy.deepcopy(items)
items1.sort(key=unitCost, reverse=True)

# print(greedy(W, items))
print(greedyFast(W, items1))
'''

'''
r1, r2 = map(int, input().split())
while 1:
  n = randint(1, r1)
  W = randint(0, r2)
  
  items = []
  for i in range(n):
    items.append([randint(0, r2), randint(1, r2)])
  items1 = copy.deepcopy(items)
  items1.sort(key=unitCost, reverse=True)
  
  if greedy(W, items) == greedyFast(W, items1):
    print("start--------------", n, W, items, " - ok")
  else:
    print("start--------------", n, W, items, " - fail")
    break
'''

file = open('sample/3_2_loot.in', 'r')
n, W = map(int, (file.readline()).split())
items = []
while True:
  line = file.readline()
  if line == '':
    break
  else:
    items.append( [*map(int, line.split())] )
file.close()

items.sort(key=unitCost, reverse=True)

for item in items:
  print(item[0], item[1], item[0] / item[1])

# print(greedyFast(W, items))


