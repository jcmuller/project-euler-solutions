def F():
  F=[]
  while True:
    if not F:
      F.append(1)
      yield F[0]
      F.append(2)
    yield F[1]
    F.append(sum(F))
    F.pop(0)
f = F()
S = 0
while True:
  v = f.next()
  if v > 4*10**6: break
  if v%2==0: S+=v
print S 
