from math import factorial

print sum([True for n in range(1,101) for r in range(1,n) if factorial(n)/(factorial(r)*factorial(n-r)) > 10**6])
