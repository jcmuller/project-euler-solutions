from math import factorial
from itertools import combinations, product

F = [factorial(n) for n in range(10)]

sol = []
for i in range(2,8):
  for n in range(10**i, 10**(i+1)):
    if n==sum([F[int(x)] for x in str(n)]):
      sol.append(n)

print sum(sol)
