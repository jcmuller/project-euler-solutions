from itertools import combinations, permutations
from sys import exit

def is_prime(N):
  if N%2==0: return False
  n = 3
  while n < N/2:
    if N%n==0: return False
    n+=1
  return True

sol = (0,0)
for p in range(9,4,-1):
  for c in combinations(range(1,p+1)[::-1], p):
    for perm in permutations(c):
      if perm[-1] in [2,4,5,6,8]: continue
      n = int(''.join([str(s) for s in perm]))
      if is_prime(n):
        print n 
        exit()

