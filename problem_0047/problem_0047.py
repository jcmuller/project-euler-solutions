from sys import exit

def factor(n):
  if n == 1: return [1]
  i = 2
  limit = n**0.5
  while i <= limit:
    if n % i == 0:
      ret = factor(n/i)
      ret.append(i)
      return ret
    i += 1
  return [n]

target = 4
n = 3
F = set()
F_count = 0
while F_count<target:
  n+=1
  factors = factor(n)
  factors = [f**factors.count(f) for f in set(factors)]
  if len(F.intersection(factors)) > 0 or len(factors)!=target:
    F = set()
    F_count = 0
    continue
  for f in factors: F.add(f)
  F_count+=1

print n-(target-1)
