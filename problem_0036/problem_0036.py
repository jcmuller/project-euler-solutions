s = 0
for n in range(1,10**6):
  if str(n)==str(n)[::-1] and bin(n)[2:]==bin(n)[:1:-1]: s+=n
print s
