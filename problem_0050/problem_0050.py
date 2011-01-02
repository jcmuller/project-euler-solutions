import sys
sys.path.append('../_resources/')
from resources import primes

P = primes(10**6)
print(len(P))
sol = (0,0)
for p in P:
  t = 0
  i = 0
  for n in P[P.index(p):]:
    if t > P[-1]: break
    t+=n
    i+=1
    if t<sol[1]: continue
    if t not in P: continue
    if i>sol[0]:
      sol=(i,t)
      print sol
print sol

'''
for i in [1]:
  for start in [s for s in P if s<p]:
    i = 0
    t = 0
    while t<p:
      t+=P[P.index(start)+i]
      i+=1
    if t==p and i>sol[0]:
      sol=(i,p)
      print sol
      break
'''
print sol
