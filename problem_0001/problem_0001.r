s = 0
for (n in 1:1000-1){
  if (n%%5==0 || n%%3==0){
    s = s+n
  }
}
print(s)
