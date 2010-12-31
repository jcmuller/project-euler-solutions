from collections import deque

def primes(n): 
  if n==2: return [2]
  elif n<2: return []
  s=range(3,n+1,2)
  mroot = n ** 0.5
  half=(n+1)/2-1
  i=0
  m=3
  while m <= mroot:
    if s[i]:
      j=(m*m-3)/2
      s[j]=0
      while j<half:
        s[j]=0
        j+=m
    i=i+1
    m=2*i+3
  return [2]+[x for x in s if x]

sol = 0
P = set(primes(10**6))
for p in P:
  is_circular = True
  l = deque([c for c in str(p)])
  if len(l)==1:
    sol+=1
    continue
  for i in range(len(l)-1):
    l.rotate()
    n = int(''.join([c for c in list(l)]))
    if not n in P:
      is_circular = False
      break
  if is_circular: sol+=1
print sol
