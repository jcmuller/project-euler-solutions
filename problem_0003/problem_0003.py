import sys
N = 600851475143
prime_factors = []
while True:
  abort = True
  i = 2
  while i<N:
    if N%i==0:
      prime_factors.append(i)
      N=N/i
      abort = False
      break
    i+=1
  if abort:
    prime_factors.append(N)
    print prime_factors[-1]
    sys.exit()
