using System;

public class Problem_1
{
  public static void Main(string[] args) {
    int sum = 0;
    for (int n=1; n<1000; n++){
      if (n%3==0 || n%5==0) sum+=n;
    }
    Console.Write(sum);
  }
}
