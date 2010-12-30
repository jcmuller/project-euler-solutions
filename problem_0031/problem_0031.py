change = (200, 100, 50, 20, 10, 5, 2, 1)
target = 200

def make_change(start_amount, change=change):
  sol = 0
  for c in change:
    if start_amount+c > target: continue
    for amount in range(start_amount+c, target+1, c):
      if amount==target:
        sol+=1
        continue
      if c>change[-1]:
        sol+=make_change(amount, change=change[change.index(c)+1:])
  return sol

print make_change(0)  
