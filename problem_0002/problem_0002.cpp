#include <iostream>

using namespace std;

int main(){
  int sum = 0;
  int a = 0;
  int b = 1;
  while (b < 4000000){
    if (b % 2 == 0){
      sum += b;
    }
    b = b + a;
    a = b - a;
  }
  cout << sum << endl;
  return 0; 
}
