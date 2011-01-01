#!/usr/bin/perl

use strict;
use warnings;

for my $i (1..1000)
{
	for my $j ($i..1000)
	{
		my $k = sqrt($i**2 + $j**2);

		if ($i + $j + $k == 1000)
		{
			printf "%d x %d x %d = %d\n", $i, $j, $k, $i * $j * $k;
			exit;
		}
	}
}
