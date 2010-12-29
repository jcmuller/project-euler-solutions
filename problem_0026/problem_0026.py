sol = []
for N in range(1,1000):
  rem = set()
  r = 1
  for i,k in enumerate(range(1000)):
    q,r = divmod(r,N)
    if r in rem and r !=0:
      sol.append({'number': N,
                  'cycles': len(rem)}) 
      break
    if i>0: rem.add(r)
    r *= 10
print sorted(sol, key= lambda x: x['cycles'])[-1]['number']
