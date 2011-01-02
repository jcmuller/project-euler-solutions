#!/usr/bin/perl

use strict;
use warnings;

for my $i (1..1000)
{
	for my $j ($i..1000)
	{
		for my $k ($j..1000)
		{
			if ($i + $j + $k == 1000)
			{
				if ($i**2 + $j**2 == $k**2)
				{
					printf "%d x %d x %d = %d\n", $i, $j, $k, $i * $j * $k;
					exit;
				}
			}
		}
	}
}
