-export([main/1]).

main(_) -> io:fwrite("~p",[fib(1,1)]).

fib(A,B) when A+B > 4000000 -> 1;
fib(A,B) when (A+B) rem 2 == 0 -> A+B + fib(B,A+B);
fib(A,B) -> fib(B,A+B).
