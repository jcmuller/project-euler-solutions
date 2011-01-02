s = 0
(1..1000).each do |i|
	s = s + i ** i
end

puts "#{s}".reverse[0..9].reverse
