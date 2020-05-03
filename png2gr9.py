from PIL import Image
with Image.open("qlka.png") as image:
	for y in range(32):
		print("\tdta\t", end="")
		for x in range(0, 32, 2):
			print("$%02x" % ((image.getpixel((x, y)) & 0xf0) | image.getpixel((x + 1, y)) >> 4), end="\n" if x == 30 else ",")

