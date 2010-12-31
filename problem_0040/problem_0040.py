from numpy import prod
l=''
i=1
while len(l)<10**6:
  l+=str(i)
  i+=1
print prod([int(l[10**p-1]) for p in range(0,6)])
