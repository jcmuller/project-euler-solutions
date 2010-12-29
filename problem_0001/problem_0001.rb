s=0
for i in (1..1000-1)
  if i%3==0 or i%5==0 then
    s+=i
  end
end  
print s
