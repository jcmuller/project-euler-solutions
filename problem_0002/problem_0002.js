#!env node

var s = 0;
a = 0;
b = 1;
while (b < 4000000){
  if (b % 2 == 0){
    s += b;
  }
  b = b + a;
  a = b - a;
}

console.log(s);
