
'''
def mult_divide_and_conquer_4 (a, b, n):
  print('enter: ', a, b, n)

  if n == 1:
    val1 = 0 if len(a) == 0 else a[0]
    val2 = 0 if len(b) == 0 else b[0]
    print('n == 1: ---------------------------- ', a, b, val1, val2)
    temp = [ val1 * val2 ]
    return temp
  
  d = n//2
  print('d: ' , d)

  aLow = a[0:d]
  bLow =  b[0:d]
  aHigh = a[d:2*d]
  bHigh = b[d:2*d]
  
  print('split array: ', aLow, bLow, aHigh, bHigh)
  
  lowAB = mult_divide_and_conquer_4(aLow, bLow, d)
  lowAHighB = mult_divide_and_conquer_4(aLow, bHigh, d)
  highALowB = mult_divide_and_conquer_4(aHigh, bLow, d)
  highAB = mult_divide_and_conquer_4(aHigh, bHigh, d)
  
  print('multiply: ', lowAB, lowAHighB, highALowB, highAB)
  
  ab = [0] * (2 * n - 1)
  for i in range(n - 1):
    ab[i] += lowAB[i]
    ab[i + d] += lowAHighB[i] + highALowB[i]
    ab[i + 2*d] += highAB[i]
  
  print('ab: ', ab)
  
  return ab
'''



def mult(a, b, n, ai, bi):
  print('enter: ', n, ai, bi)
  
  r = [0] * (2 * n - 1)
  print('init r: ', r)
  
  if n == 1:
    val1 = 0 if len(a) <= ai else a[ai]
    val2 = 0 if len(b) <= bi else b[bi]
    r[0] = val1 * val2
    print('n == 1: ', ai, bi, r)
    return r
  
  d = n//2
  
  r[0 : n - 2] = mult(a, b, d, ai, bi)
  r[n : 2 * n - 2] = mult(a, b, d, ai + d, bi + d)
  D0E1 = mult(a, b, d, ai, bi + d)
  D1E0 = mult(a, b, d, ai + d, bi)
  
  print('put into r---------------------', d, n+d-1)
  j = 0
  for i in range(d, n + d - 1):
    r[i] += D0E1[j] + D1E0[j]
    print('inside: ',i, r)
    j += 1
  
  return r

  

coefficient = 4
a = [3, 2, 5]
b = [5, 1, 2]
# print(mult_divide_and_conquer_4 (a, b, coefficient))
print(mult(a, b, coefficient, 0, 0))
