#!/usr/bin/perl
use strict;
use warnings;

use lib '../_resources';
use resources 'is_palin';

my $sum = 0;
for my $i (1..10**6 - 1)
{
	if (is_palin($i))
	{
		my $b = sprintf("%b", $i);
		if (is_palin($b))
		{
			#print "$i $b\n";
			$sum += $i;
		}
	}
}

print "$sum\n";
