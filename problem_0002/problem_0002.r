F <- function(N){
  if (N<3){return(1)}
  a = c(1,1)
  for (n in c(3:N)){
    a = append(a, sum(a))
    a = a[2:3]
  }
  return(a[2])
}

S = i = 0
while(TRUE){
  v = F(i)
  if (v>4*10**6){break}
  if (v%%2==0){S=S+v}
  i = i+1
}
print(S)
