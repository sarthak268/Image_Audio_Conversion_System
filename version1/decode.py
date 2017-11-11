from PIL import Image
import scipy.io.wavfile as wave
import numpy

filename = raw_input()
im = Image.open(filename)

left = []
right = []

for i in range(im.size[0]):
	for j in range(im.size[1]):
		pixel = im.getpixel((i, j))
		r = pixel[0]
		g = pixel[1]
		b = pixel[2]

		if (b == 64):
			r *= -1
			g *= -1
		
		elif (b == 128):
			r *= -1

		elif (b == 192):
			g *= -1

		r *= 4
		g *= 4

		left.append(r)
		right.append(g)


y = []
for i in range(len(left)):
	y.append([left[i], right[i]])

y = numpy.array(y, dtype='int16')

wave.write('amyout.wav', 44100, y)