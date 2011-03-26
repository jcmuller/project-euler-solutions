#!env node

var s = 0;
for (var n=0; n<1000; n++){
  if (n%3==0 || n%5==0){
    s += n
  }
}
console.log(s)
