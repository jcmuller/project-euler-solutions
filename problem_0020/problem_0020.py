from math import factorial

N = factorial(100)
S = 0
for c in str(N):
 S += int(c)
print S
