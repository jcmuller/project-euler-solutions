def solve():
  rng = range(11,21)
  i = 20
  while True:
    done = True
    for n in rng:
      if i%n!=0:
        done = False
        i += 20
        break
    if done:
      return i

if __name__ == '__main__':
  print solve()
