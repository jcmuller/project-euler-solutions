def divisors(N):
  d = []
  for n in range(1,N/2+1):
    if N%n==0: d.append(n)
  return d

def solve(N):
  S = 0
  for n in range(1,N):
    s_1 = sum(divisors(n))
    s_2 = sum(divisors(s_1))
    if n == s_2 and n != s_1:
      S += n  
  return S  

if __name__ == '__main__':
  print solve(10000)
