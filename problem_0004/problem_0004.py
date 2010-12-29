def solve():
  sol = []
  for i in range(100,999):
    for j in range(i,999):
      p = '%i'%(i*j)
      if p==p[::-1]:
        sol.append(i*j)
  return sorted(sol)

if __name__=='__main__':
  print solve()[-1]
