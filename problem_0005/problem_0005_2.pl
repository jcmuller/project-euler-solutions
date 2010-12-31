#!/usr/bin/perl 
use strict;
use warnings;

# Brute force method. Since the smallest number evenly divisible for N<=10 is
# 2520, start from there.

my $n = 2520;

sub get_lcm
{
	my ($a, $b) = @_;
	return ($a * $b) / get_gcd($a, $b);
}

sub get_gcd
{
	my ($small, $large) = sort {$a <=> $b} @_;
	my $tmp;
	while (1)
	{
		$tmp = $large - $small;
		$large = $small;
		$small = $tmp;
		return $large if ($small == 0);
		($small, $large) = sort {$a <=> $b} ($small, $large);
	}
}

my ($a, $b, $l, $g);
$l = 2;

for (2..20)
{
	$l = get_lcm($_, $l);
}

print "$l\n";
