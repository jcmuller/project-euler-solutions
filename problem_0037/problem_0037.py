def primes(n): 
  if n==2: return [2]
  elif n<2: return []
  s=range(3,n+1,2)
  mroot = n ** 0.5
  half=(n+1)/2-1
  i=0
  m=3
  while m <= mroot:
    if s[i]:
      j=(m*m-3)/2
      s[j]=0
      while j<half:
        s[j]=0
        j+=m
    i=i+1
    m=2*i+3
  return [2]+[x for x in s if x]

sol = 0
P = set(primes(10**6))
for p in list(P):
  if p<10: continue
  s_l = p
  s_r = p
  while True:
    s_r = int(str(s_r)[:-1])
    s_l = int(str(s_l)[1:])
    if not s_r in P or not s_l in P: break
    if s_r<10:
      sol += p
      break
print sol
