def get_next(n)
	if n % 2 == 0
		n/2
	else
		3 * n + 1
	end
end

def seq(n)
	a = [n]
	while (n > 1)
		n = get_next(n)
		a << n
	end

	a
end

max = 0
initial = 0
longest = []

(10**5..10**6).to_a.reverse.each do |i|
	se = seq(i)
	s = se.size

	#puts "seq=" + se.inspect + " i=#{i} size=#{s}"

	if s > max
		longest = se
		max = s
		initial = i
	end
end

puts "max=#{max} initial=#{initial}"
