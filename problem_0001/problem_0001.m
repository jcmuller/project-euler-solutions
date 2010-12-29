s=0;
for n=1:1000-1
  if mod(n,5)==0 || mod(n,3)==0
    s += n;
  end
end
disp(s)
