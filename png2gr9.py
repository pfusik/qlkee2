def nibble(image, x, y):
	if (x - 16) **2 + (y - 16) ** 2 >= 225: return 0
	p = image.getpixel((x, y)) >> 4
	if p == 0: return 1
	return p

from PIL import Image
with Image.open("qlka.png") as image:
	for y in range(32):
		print("\tdta\t", end="")
		for x in range(0, 32, 2):
			print("$%02x" % (nibble(image, x, y) << 4 | nibble(image, x + 1, y)), end="\n" if x == 30 else ",")

