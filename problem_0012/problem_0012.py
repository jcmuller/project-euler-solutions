from numpy import prod
def factor(n):
  yield 1
  i = 2
  limit = n/2
  while i <= limit:
    if n % i == 0:
      yield i
    i += 1
  if n > 1:
    yield n

def solve():
  N = 1
  i = 1
  while True:
    factors = [j for j in factor(N)]
    if len(factors)>500: return N
    i += 1
    N += i

if __name__ == '__main__':
  print solve()
