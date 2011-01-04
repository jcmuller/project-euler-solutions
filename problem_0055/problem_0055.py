def is_lychrel(N):
  if N>10 and str([N])[-1]=='0': return False
  for i in range(50):
    print N
    print int(str(N)[::-1])
    N = N + int(str(N)[::-1])
    if str(N)==str(N)[::-1]:  return True
  return False

print sum([True for n in range(,11) if is_lychrel(n)])
