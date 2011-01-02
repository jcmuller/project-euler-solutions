from sys import exit
sol =0 
for i in range(999,100,-1):
  for j in range(999,i,-1):
    if i*j<sol: break
    p = '%i'%(i*j)
    if p==p[::-1]:
      sol = max(sol,i*j)
      break
print sol
