# Note: solve() was used to generate the number of paths for small
# grids (2,3,...8). However, when solving for larger grids (20),
# it is not practical to solve by hand. Instead, the function was
# extracted from the smaller sets (through observation) in order to
# calculate the formula:
#
#   xi = 3*xi+xi*i/(i+2)
#
# where i is the iteration step. This led to:
#
#   n  i  paths
#   -  -  -----
#   2  1  6
#   3  2  20
#   4  3  70
#   5  4  252
#   6  5  924
#   7  6  3432
#   8  7  12870
#   .  .  
#  20 19  137846528820

def solve(size=(20,20), loc=(0,0)):
  if loc==size: return 1
  return (solve(loc=(loc[0]+1, loc[1]+0), size=size) if loc[0]<size[0] else 0)+ \
         (solve(loc=(loc[0]+0, loc[1]+1), size=size) if loc[1]<size[1] else 0)

def solve_approx(N):
  i=1
  x=6
  for n in range(2,N):
    x = 3*x+x*i/float(i+2)
    i +=1
  return x
  
if __name__ == '__main__':
  print solve_approx(20)
