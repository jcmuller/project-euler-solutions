import sys
sys.path.append('../_resources/')
from resources import primes
from itertools import permutations, combinations
P = [p for p in primes(10**4) if p > 10**3]

for p in P:
  S = sorted(list(set([int(''.join(x)) for x in permutations(str(p)) if int(''.join(x)) in P and x[0]!='0'])))
  if 1487 in S: continue
  if len(S) >= 3:
    D = [abs(p-x) for x in S]
    if len(set(D))==len(D): continue 
    R = [p]+sorted(list(set([s for d,s in zip(D,S) if D.count(d)>=2])))
    print ''.join([str(r) for r in sorted(R)])
    break
