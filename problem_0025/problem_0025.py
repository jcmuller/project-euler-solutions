def solve():
  def Fib():
    F = [1,1]
    while True:
      yield F[1]
      F.append(sum(F)) 
      F.pop(0)
  
  F = Fib() 
  i = 1
  while True:
   f = F.next()
   i += 1
   if len(str(f))==1000: return i    

if __name__ == '__main__':
  print solve()
