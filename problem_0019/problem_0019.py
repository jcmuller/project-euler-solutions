from datetime import date, timedelta

start = date(1901, 1, 1)
end   = date(2000, 12, 31)

sol = 0

for d in range((end-start).days+1):
  D = start+timedelta(days=d)
  sol += 1 if D.weekday()==6 and D.day==1 else 0

print sol 
