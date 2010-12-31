t = [0.5*n*(n+1) for n in range(200)]

f = open('words.txt')
l = f.readline().rstrip().replace('"','')
words = l.split(',')
f.close()

sol = 0
for word in words:
  s = sum([ord(x)-64 for x in word])
  if s in t: sol+=1

print sol
