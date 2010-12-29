-export([main/1]).

main(_) -> io:fwrite("~p",[func(1)]).

func(1000) -> 0;
func(N) when (N rem 3 == 0) or (N rem 5 == 0) -> N+func(N+1);
func(N) -> func(N+1).
