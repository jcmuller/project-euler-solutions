#! env python

def F(limit=float('Inf')):
  a=0
  b=1
  while a+b<limit:
   if (a+b)%2==0: yield a+b
   a,b = b,a+b

f = F(4*10**6)
print sum(f)
