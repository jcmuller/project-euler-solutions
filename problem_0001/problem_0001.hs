main = do
  print $ sum [ if x `mod` 3 == 0 || x `mod` 5 == 0 then x else 0 | x<-[1..1000-1]]
