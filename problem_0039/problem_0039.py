sol = (0,0)
for p in range(1000+1):
  s = 0
  for a in range(1, p-2):
    for b in range(1,a):
      c = (a**2+b**2)**.5
      if a+b+c>p: break
      if a+b+c==p: s+=1
  if s>sol[1]: sol=(p,s)
print sol[0]
