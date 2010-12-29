from itertools import permutations
n = ''.join([str(n) for n in range(10)])
p = sorted([p for p in permutations(n,10)])
print p[1000000-1]
