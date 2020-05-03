R = 12

def nibble(image, x, y):
	if (x - R) **2 + (y - R) ** 2 >= (R - 1) ** 2: return 0
	p = image.getpixel((x, y)) >> 4
	if p == 0: return 1
	return p

from PIL import Image
with Image.open("qlka.png") as image:
	for y in range(2 * R):
		print("\tdta\t", end="")
		for x in range(0, 2 * R, 2):
			print("$%02x" % (nibble(image, x, y) << 4 | nibble(image, x + 1, y)), end="\n" if x == 2 * R - 2 else ",")

