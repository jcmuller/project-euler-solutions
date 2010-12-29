def is_prime(N):
  i = 2
  while i<N/2:
    if N%i==0:
      return False
    i+=1
  return True

i = 2 
n = 3
while i!=10001:
  n+=2
  if is_prime(n): i+=1    
print n
