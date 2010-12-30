function output = F(N)
  if N<3
     output = 1;
     break
  end
  a = [1,1];
  for i=3:N
    a = [a sum(a)];
    a = a(2:3);
  end
  output = a(2);
end

S=v=i=0;
while v<4*10**6
  i += 1;
  v = F(i);
  if mod(v,2)==0
    S += v;
  end
end

disp(S)
