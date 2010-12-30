sol = 1
for a in range(10,99):
  if a%10==0 or a%11==0: continue
  A = set(str(a))
  for b in range(a,100):
    if b%10==0 or b%11==0: continue
    B = set(str(b))
    if len(A.intersection(B)) != 1: continue
    c = list(A.intersection(B))[0]
    a_new,b_new = [int(str(x).replace(c,'')) for x in a,b]
    if a/float(b)==a_new/float(b_new): sol*=a/float(b)
print 1/sol 
