#!/usr/bin/perl 
use strict;
use warnings;

sub is_multiple
{
	my ($n) = @_;

	return 1 if ($n % 3 == 0);
	return 1 if ($n % 5 == 0);
	return 0;
}

my $sum = 0;
for (1..999)
{
	$sum += $_ if (is_multiple($_));
}

print "$sum\n";
