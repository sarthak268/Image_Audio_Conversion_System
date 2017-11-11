from PIL import Image
blendimage = Image.open('blendin.png')
mountains = Image.open('underlay.png')
deblend = Image.new("RGB", (936, 936), "black")

pixelsblend = blendimage.load()
pixelsmountain = mountains.load()
pixelsdeblend = deblend.load()

for i in range(936):
	for j in range(936):
		r1, g1, b1 = pixelsblend[i, j]
		r2, g2, b2, a2 = pixelsmountain[i, j]
		r3 = int(2 * (r1 - 0.5 * r2))
		g3 = int(2 * (g1 - 0.5 * g2))
		b3 = b1

		pixelsdeblend[i, j] = (r3, g3, b3)

deblend.save('deblend.png')
