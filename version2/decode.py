from PIL import Image
import scipy.io.wavfile as wave
import numpy

left = []
right = []
channel = 0

filename = raw_input()
audiofile = raw_input()
im = Image.open(filename)

for i in range(im.size[0]):
	for j in range(im.size[1]):
		pixel = im.getpixel((i, j))
		r = pixel[0]
		g = pixel[1]
		b = pixel[2]

		leftpart = bin(r)[2:]
		leftpart = '0' * (8 - len(leftpart)) + leftpart
		rightpart = bin(g)[2:]
		rightpart = '0' * (8 - len(rightpart)) + rightpart

		numbin = '0b' + leftpart + rightpart
		num = int(numbin, 2)
		if (b == 2):
			num *= -1
			
		if (channel == 0):
			left.append(num)

		if (channel == 1):
			right.append(num)
		
		channel = 1 - channel

y = []
for i in range(len(left)):
	y.append([left[i], right[i]])

y = numpy.array(y, dtype='int16')

wave.write(audiofile, 44100, y)
