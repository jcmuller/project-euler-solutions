def is_prime(n)
	if n == 1
		return false
	elsif n < 4
		return true
	elsif n % 2 == 0
		return false
	elsif n < 9
		return true
	elsif n % 3 == 0
		return false
	end

	r = (Math.sqrt(n)).floor
	f = 5
	while (f <= r)
		if n % f == 0
			return false
		elsif n % (f + 2) == 0
			return false
		end

		f += 6
	end

	return true
end

def get_primes_up_to(max)
	primes = [2]
	count = 1
	candidate = 1

	while (candidate < max)
		if is_prime(candidate)
			primes << candidate
		end
		candidate += 2
	end

	return primes
end

