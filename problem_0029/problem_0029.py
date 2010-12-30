from itertools import product

sol = set()
for a,b in product(range(2,100+1), range(2,100+1)):
  sol.add(a**b)
print len(sol)
