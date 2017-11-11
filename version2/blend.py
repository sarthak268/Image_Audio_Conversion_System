from PIL import Image
im1 = Image.open('underlay.png')
im2 = Image.open('amy.png')
im = Image.new("RGB", (936, 936), "black")

pixel1 = im1.load()
pixel2 = im2.load()
pixelblend = im.load()
for i in range(936):
	for j in range(936):
		r1, g1, b1, a1 = pixel1[i, j]
		r2, g2, b2 = pixel2[i, j]
		r3 = int(0.5 * (r1 + r2))
		g3 = int(0.5 * (g1 + g2))
		b3 = b2
		pixelblend[i, j] = (r3, g3, b3)

im.save('blend.png')
