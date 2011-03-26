#! env ruby

s=0
a=0
b=1
while b < 4*10**6 do
  a,b = b,a+b
  if b%2==0 then
    s+=b
  end
end  
print s
