def is_prime(N):
#  return all([N%n for n in range(2,N/2)])
  i = 2
  while i<N/2:
    if N%i==0:
      return False
    i+=1
  return True

def solve():
  i = 2 
  n = 3

  while i!=10001:
    n+=2
    if is_prime(n):
      i+=1    
      print i
  return n

if __name__ == '__main__':
  print solve()
