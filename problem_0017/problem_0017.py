def solve(N):
  key =  { 1: 'one',
           2: 'two',
           3: 'three',
           4: 'four',
           5: 'five',
           6: 'six',
           7: 'seven',
           8: 'eight',
           9: 'nine',
          10: 'ten',
          11: 'eleven',
          12: 'twelve',
          13: 'thirteen',
          14: 'fourteen',
          15: 'fifteen',
          16: 'sixteen',
          17: 'seventeen',
          18: 'eighteen',
          19: 'nineteen'}

  for k,v in dict(zip(range(20,100,10), ['twenty','thirty','forty','fifty', \
                                   'sixty','seventy','eighty','ninety'])).iteritems():
    for i in range(10):
      if i==0:
        key[k]=v
      else:
        key[k+i]=v+key[i]

  for i in range(100,1000,100):
    for j in range(100):
      if j==0:
        key[i]=key[i/100]+'hundred'
      else:
        key[i+j] = key[i/100]+'hundredand'+key[j]

  key[1000] = 'onethousand' 
  
  C = 0
  for n in range(1,N+1):
    C += len(key[n])
  return C

if __name__ == '__main__':
  print solve(1000)
