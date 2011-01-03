from itertools import permutations

n = 10
while True:
  n+=1
  s = str(n)
  S = set([int(''.join(p)) for p in permutations(s)])
  if all([n*i in S for i in range(2,7)]):
    print n
    break
