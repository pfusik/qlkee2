R = 12

def nibble(image, x, y):
	if (x - R + .5) **2 + (y - R + .5) ** 2 >= 12 ** 2: return 0
	p = image.getpixel((2 + x, 2 + y)) >> 4
	if p == 0: return 1
	return p

from PIL import Image
with Image.open("qlka.png") as image:
	for y in range(2 * R):
		print("\tdta\t", end="")
		for x in range(0, 2 * R, 2):
			print("$%02x" % (nibble(image, x, y) << 4 | nibble(image, x + 1, y)), end="\n" if x == 2 * R - 2 else ",")

