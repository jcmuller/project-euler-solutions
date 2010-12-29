s = 0
for n in range(1000):
   s += n if n%5==0 or n%3==0 else 0
print s
