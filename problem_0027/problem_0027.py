def is_prime(N):
  if N<1: return False
  for n in range(2,N/2):
    if N%n==0: return False
  return True

def QF(a,b):
  n = 0
  while True:
    yield n**2+a*n+b
    n+=1

sol = []

for a in range(-999,1000):
  for b in range(-999,1000):
    i  = 0
    qf = QF(a,b)
    while True:
      v = qf.next()
      i += 1
      if not is_prime(v):
        sol.append({'a': a,
                    'b': b,
                    'i': i-1})
        break

print sorted(sol, key=lambda x: x['i'])[-1]
