n = d = 1
s = 0
for i in range(1000):
  n,d  = (n+2*d,d+n)
  if len(str(n)) > len(str(d)): s+=1
print s
