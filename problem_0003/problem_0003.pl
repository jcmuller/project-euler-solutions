#!/usr/bin/perl
use strict;
use warnings;

my $n = 600851475143;
my $i = 1;

while (++$i < $n)
{
	$n /= $i if ($n % $i == 0);
}

print "$n\n";
