def solve(N):
  S = 0
  for c in str(N):
    S+=int(c)
  return S

if __name__ == '__main__':
  print solve(2**1000)
