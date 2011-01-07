using System;

public class Problem_2
{
  public static void Main(string[] args) {
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
    Console.Write(sum);
  }
}
