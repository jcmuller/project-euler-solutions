def solve(N):
  sum_of_squares = sum([n**2 for n in range(1,N+1)])
  square_of_sum  = sum(range(1,N+1))**2
  return square_of_sum-sum_of_squares

if __name__ == '__main__':
  print solve(100)
