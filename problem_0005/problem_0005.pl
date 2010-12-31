#!/usr/bin/perl
use strict;
use warnings;

# The smallest number evenly divisible by all the integers up to 20 will be the
# LCM of all of them.

my %powers;

# All the primes up to N, which for this problem is 20.
my @primes = (2, 3, 5, 7, 9, 11, 13, 17, 19);

for my $n (2..20)
{
	my %lpowers;
	my $v = $n;
	for my $p (@primes)
	{
		while ($v % $p == 0)
		{
			$lpowers{$p}++;
			$v /= $p;
		}
	}

	while (my ($base, $power) = each %lpowers)
	{
		$powers{$base} ||= 0;
		$powers{$base} = $power if ($powers{$base} < $power);
	}
}

my $sol = 1;

while (my ($base, $power) = each %powers)
{
	$sol *= $base ** $power;
}

print "$sol\n";

