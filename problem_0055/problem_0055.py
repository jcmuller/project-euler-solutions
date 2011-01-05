def is_lychrel(N):
  if str([N])[-1]=='0': return False
  for i in range(50):
    N += int(str(N)[::-1])
    if str(N)==str(N)[::-1]:  return False
  return True

print sum([True for n in range(10**4) if is_lychrel(n)])
