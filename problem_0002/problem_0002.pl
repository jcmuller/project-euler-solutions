#!/usr/bin/perl 
use strict;
use warnings;

sub fibo
{
	my ($num) = @_;
	my $root = sqrt(5);

	return int ( ( 1/$root * ( ( ( ( 1 + $root ) / 2 ) ** $num ) - ( ( ( 1 - $root ) / 2 ) ** $num ) ) ) );
}

my $max = 4 * 10**6;
my $fib;
my $total = 0;
my $i = 0;

while ($fib < $max)
{
	$i++;
	$fib = fibo($i);
	last if ($fib >= $max);

	if ($fib % 2 == 0)
	{
		$total += $fib;
		printf("fib(%2d) = %d\n", $i, $fib);
	}
}

print "Total: $total\n";

