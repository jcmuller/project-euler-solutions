from numpy import prod
import sys

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

N = 1
i = 1
while True:
  factors = [j for j in factor(N)]
  if len(factors)>500:
    print N
    sys.exit()
  i += 1
  N += i
