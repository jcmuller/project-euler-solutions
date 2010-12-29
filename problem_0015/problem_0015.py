def choose(n, k):
  ntok = 1
  for t in xrange(min(k, n-k)):
    ntok = ntok*(n-t)//(t+1)
  return ntok
print choose(40,20)
