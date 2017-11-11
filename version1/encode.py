from PIL import Image
import scipy.io.wavfile as wave
import numpy

audiofile = raw_input()
samplingRate, audioChannels = wave.read(audiofile)

left = list(audioChannels[:, 0])
right = list(audioChannels[:, 1])

mleft = max(map(abs, left))
mright = max(map(abs, right))

def divide(a):
	return (a / float(mleft)) * 255

left = map(divide, left)

def divide(a):
	return (a / float(mright)) * 255

right = map(divide, right)

im = Image.new("RGB", (670, 670), "black")


ai = 0
done = False
for i in range(670):
	if done:
		break
	for j in range(670):
		if ai >= 437744:
			done = True
			break
		r = int(left[ai])
		g = int(right[ai])
		b = 0
		if (r == 0 and g == 0):
			b = 0
		elif (r < 0 and g < 0):
			b = 64
		elif (r < 0 and g >= 0):
			b = 128
		elif (r >= 0 and g < 0):
			b = 192
		else:
			b = 255
		im.putpixel((i, j), (r, g, b))
		ai += 1

im.save('amy.bmp')