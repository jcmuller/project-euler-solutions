def triangle():
  n = 1
  while True:
    yield n*(n+1)/2
    n+=1

def pentagonal():
  n = 1
  while True:
    yield n*(3*n-1)/2
    n+=1

def hexagonal():
  n = 1
  while True:
    yield n*(2*n-1)
    n+=1

T = triangle()
P = pentagonal()
H = hexagonal()

t = T.next()
p = P.next()
h = H.next()

while t!=p or t!=h or t<=40755:
  t = T.next()
  while p < t: p = P.next()
  while h < t: h = H.next()

print t
