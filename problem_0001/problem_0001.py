def solve():
  s = 0
  for n in range(1000):
   if n%5==0 or n%3==0:
     s += n
  print s 

if __name__ == '__main__':
  solve()
