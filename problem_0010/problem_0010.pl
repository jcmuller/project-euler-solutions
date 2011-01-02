#!/usr/bin/perl
use strict;
use warnings;
use feature 'switch';

# Use algorithm described in the solutions

sub isPrime
{
	my $n = shift;

	given ($n)
	{
		when (1          ) { return 0; }
		when ($n < 4     ) { return 1; }
		when ($n % 2 == 0) { return 0; }
		when ($n < 9     ) { return 1; }
		when ($n % 3 == 0) { return 0; }
	}

	my $r = int (sqrt($n));
	my $f = 5;

	while ($f <= $r)
	{
		return 0 if ($n % $f == 0);
		return 0 if ($n % ($f + 2) == 0);
		$f += 6;
	}

	return 1;
}

my $limit = 2 * 10**6;
my $candidate = 1;
my $sum = 2;

while ($candidate < $limit)
{
	$candidate += 2;
	if (isPrime($candidate))
	{
		$sum += $candidate;
	}
}

print "$sum\n";

