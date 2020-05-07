sub put($) {
	my ($x) = @_;
	$x += 16 * $i;
	$x = 0 if $x < 0;
	$x = 255 if $x > 255;
	print F chr $x;
#	printf '%02x ', $x;
}

open F, '>generated.pal' and binmode F or die;
for $h (0..15) {
	$a = $h * 6.28 / 16;
	for $i (0..15) {
		put(127 * sin($a));
		put(127/4 * cos($a) - 127/2 * sin($a));
		put(-127 * cos($a));
	}
#	print "\n";
}
__END__

sat = 70
u = sat * cos(c)
v = sat * sin(c)
clamp(298 * i + 409 * v + 128 >> 8)
clamp(298 * i - 100 * u - 208 * v + 128 >> 8)
clamp(298 * i + 516 * u + 128 >> 8)


100 * 70 / 256 = 27 ~ 32

+ 127*sin
- 1/4*127*cos - 1/2*127*sin
+ 5/4*127*cos
