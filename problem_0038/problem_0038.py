sol = 0
n = 1
while n < 10**9:
  s = ''
  i = 0
  while len(s) < 9:
    i+=1
    s+=str(n*i)
    if len(s)==9 and int(s)>sol and i>1 and set(range(1,10)).difference([int(c) for c in s])==set():
      sol=int(s)
      print 'Solution: %i   Config: %i @ %i'%(sol,n,i)
  n+=1
