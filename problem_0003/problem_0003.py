def solve(num):
  prime_factors = []
  while True:
    abort = True
    i = 2
    while i<num:
      if num%i==0:
        prime_factors.append(i)
        num=num/i
        abort = False
        break
      i+=1
    if abort:
      prime_factors.append(num)
      return prime_factors

if __name__ == '__main__':
  print solve(600851475143)[-1]
