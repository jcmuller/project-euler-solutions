#!/usr/bin/env ruby

n = 2**1000
sum = 0
"#{n}".chars.to_a.each do |i|
	sum += i.to_i
end

puts sum
