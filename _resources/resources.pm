use strict;
use warnings;

package resources;

require Exporter;
our @ISA = qw(Exporter);
our @EXPORT_OK = qw(fibo is_palin);


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

1;
