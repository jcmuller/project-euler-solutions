def solve():
  def collatz(n, iteration=1):
    if n == 1: return iteration
    if n%2==0:
      return collatz(n/2, iteration+1)
    else:
      return collatz(3*n+1, iteration+1)

  max_i = (0,0) 
  for n in range(1,1000000)[::-1]:
    i = collatz(n)
    max_i = (n,i) if i>max_i[1] else max_i
  return max_i

if __name__ == '__main__':
  print solve()
