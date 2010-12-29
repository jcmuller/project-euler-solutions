def solve():
  f = open('names.txt')
  names = f.readline().split(',')
  names = sorted([name.replace('"','') for name in names])
  f.close()
  S = 0
  for i,name in enumerate(names):
    S += (i+1)*sum([ord(c)-64 for c in name])
  return S 

if __name__ == '__main__':
  print solve()
