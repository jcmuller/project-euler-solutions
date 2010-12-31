#!/usr/bin/perl

my $prime = 10001;
my @primes = (2);

my $i = 2; 
my $b = 1; 

while (1)
{
	for (@primes)
	{
		if ($i % $_ == 0)
		{
			$b = 1;
			next;
		}
	}
	if ($b)
	{
		$b = 0;
	}
	else
	{
		push @primes, $i;
		last if (scalar @primes == $prime);
	}
	$i++;
}

print pop @primes, "\n";
