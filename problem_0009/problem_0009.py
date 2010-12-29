import math

def solve():
  for a in range(1,1000):
    for b in range(a+1,1001):
      c = math.sqrt(a**2 + b**2)
      if a+b+c==1000:
        return int(a*b*c)

if __name__ == '__main__':
  print solve()
