import sys
sys.path.append('../_resources/')
from resources import primes
from itertools import product

# Extract out primes between 10**5 and 10**6
P = [str(p) for p in primes(10**6) if p>10**5]

# Create a list of permutation patterns
permutations = [''.join([str(x) for x in p]) for p in product(range(2), repeat=6)][1:-1]

# Create an ignore set to reduce redundent calculations 
ignore = set()

for p in P:
  for permutation in permutations:
    count = 0

    # Check if the permutation pattern as been performed before
    pattern = ''.join(['x' if i=='1' else c for c,i in zip(p,permutation)])
    if pattern in ignore: continue
    ignore.add(pattern)
    for n in range(10):
      if ''.join([c if pm=='0' else str(n) for c,pm in zip(p,permutation)]) in P: count+=1
    if count == 8:
      print p
      sys.exit(0)
