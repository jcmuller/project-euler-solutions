import sys
from itertools import cycle, permutations

f = open('cipher1.txt')
data = [int(c) for c in f.readline().strip().split(',')]
f.close()

for p in permutations(range(ord('a'), ord('z')+1), 3):
  key = cycle(p)
  msg = [char^key.next() for char in data]
  if min(msg) >= 32 and max(msg) <= 126:
    msg_text = ''.join([chr(c) for c in msg])
    if 'the' in msg_text and 'in' in msg_text and 'that' in msg_text:
      print sum(msg) 
