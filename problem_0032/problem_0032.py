sol = []
s = set(range(1,10))
for N in range(10**3, 10**4):
  c = set([int(c) for c in str(N)])
  for n in range(1,N/2):
    if N%n==0:
      a = set([int(c) for c in str(n)])
      b = set([int(c) for c in str(N/n)])
      if a.union(b).union(c)==s:
        sol.append(N)
        break
print sum(sol)
