import sys

sys.path.append('../_resources')

from resources import primes

P = primes(10**9)

def primes_in_layer():
  N = 3
  c = 0
  i = 1
  while i < len(P):
    if P[i] > N**2:
      yield c
      c=0
      N+=2
    if P[i] < N**2 and P[i] in range(N**2, (N-2)**2, -(N-1)): c+=1
    i+=1
    
r = 1.0
n = 1
S = 0.0
p = primes_in_layer()

while r > 0.10:
  n+=2
  S+=p.next()
  r=float(S)/(2*n-1)
print n
