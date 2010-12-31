from itertools import permutations

properties = [2,3,5,7,11,13,17]

def pandigital(prefix, level):
   sol = 0
   for n in set(range(10)).difference([int(c) for c in prefix]):
     i = int(prefix[-2:]+str(n))
     if not i%properties[level]==0: continue
     if level==len(properties)-1:
       sol+=int(prefix+str(n))
       continue
     sol+=pandigital(prefix+str(n), level+1)
   return sol

sol=0
for p in permutations(range(10),3):
  if p[0]==0: continue
  s = ''.join([str(c) for c in p])
  sol+=pandigital(s,0)

print sol
