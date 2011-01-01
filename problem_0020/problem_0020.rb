#!/usr/bin/env ruby

def fact(n)
	f = 1
	(1..n).each do |i|
		f *= i
	end

	f
end

n = fact(100)

sum = 0
"#{n}".chars.to_a.each do |i|
	sum += i.to_i
end

puts sum
