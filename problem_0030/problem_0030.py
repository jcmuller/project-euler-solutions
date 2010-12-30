sol = []
power_of_ten = 1
while 10**(power_of_ten) < (9**5)*(power_of_ten+1):
  for n in range(10**power_of_ten, 10**(power_of_ten+1)):
    if sum([int(c)**5 for c in str(n)]) == n:
      sol.append(n)
  power_of_ten+=1
print sum(sol)
