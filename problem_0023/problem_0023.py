def divisors(N):
  d = []
  for n in range(1,N/2+1):
    if N%n==0: d.append(n)
  return d

def solve():
  from itertools import product

  ceil = 28123
  abundant = []

  for N in range(1,ceil+1):
    if sum(divisors(N)) > N: abundant.append(N)
  return sum(list(set(range(1,ceil+1))-set([sum(d) for d in product(abundant,abundant)])))

if __name__ == '__main__':
  print solve()
