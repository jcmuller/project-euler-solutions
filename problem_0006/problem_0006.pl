#!/usr/bin/perl 
use strict;
use warnings;

sub sum
{
	my ($func, $n, $max) = @_;

	my $sum = 0;
	for ($n..$max)
	{
		$sum += $func->($_);
	}
	return $sum;
}

sub sum_numbers
{
	my ($n) = @_;
	return ($n * ($n + 1)) / 2;
}

my $limit = 100;
my $n_sq = sub {my $n = shift; return $n ** 2};
my $squares = sum($n_sq, 1, $limit);
my $sum_square = sum_numbers($limit) ** 2;

print $sum_square - $squares, "\n";
