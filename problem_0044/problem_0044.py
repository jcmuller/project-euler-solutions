from itertools import combinations
from sys import exit

def pentagonal(i=1):
  while True:
    yield i*(3*i-1)/2
    i+=1

P = set()
p = pentagonal()

while True:
  n = p.next()
  P.add(n)
  for i in P.difference([n]):
    if n-i not in P: continue
    if i+n<max(P):
      if i+n not in P: continue
    else:  
      p_2 = pentagonal(j)
      p2 = p_2.next()
      while p2 < i+n:
        p2 = p_2.next()
      if not p2==i+n: continue
    print n-i
    exit()
