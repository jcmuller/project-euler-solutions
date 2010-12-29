import sys
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
    print i
    sys.exit()
