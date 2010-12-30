diag = [1]
for i in range(2,(1001+1)/2+1):
  diag.extend([(2*i-1)**2-2*(i-1)*n for n in range(4)]) 
print sum(diag)
