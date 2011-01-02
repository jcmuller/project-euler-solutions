use strict;
use warnings;

package resources;

use feature 'switch';

require Exporter;
our @ISA = qw(Exporter);
our @EXPORT_OK = qw(fibo is_palin is_prime get_nth_prime get_primes_up_to);


sub fibo
{
	my ($num) = @_;
	my $root = sqrt(5);

	return int ( ( 1/$root * ( ( ( ( 1 + $root ) / 2 ) ** $num ) - ( ( ( 1 - $root ) / 2 ) ** $num ) ) ) );
}

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


sub is_prime
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

sub get_nth_prime
{
	my $limit = shift;
	my $count = 1;
	my $candidate = 1;

	while ($count < $limit)
	{
		$candidate += 2;
		$count++ if (is_prime($candidate));
	}

	return $candidate;
}

sub get_primes_up_to
{
	my $max = shift;

	my $primes = [2];
	my $count = 1;
	my $candidate = 1;

	while ($candidate < $max)
	{
		push @$primes, $candidate if (is_prime($candidate));
		$candidate += 2;
	}

	return $primes;
}

1;
