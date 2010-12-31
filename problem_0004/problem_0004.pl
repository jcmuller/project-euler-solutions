#!/usr/bin/perl 
use strict;
use warnings;

sub is_palin
{
	my ($q) = shift;
	my $l = int ((length $q) / 2);
	for (0..$l)
	{
		my ($f, $t) = (substr($q, $_, 1), substr($q, -$_ - 1, 1));
		return 0 if ($f ne $t);
	}
	return 1;
}

my $largest = 0;
for (my $i = 999; $i > 99; $i--)
{
	for (my $j = 999; $j > $i; $j--)
	{
		my $p = $i * $j;
		last if ($p < $largest);

		$largest = $p if (is_palin($p) and $p > $largest);
	}
}

print "$largest\n";
