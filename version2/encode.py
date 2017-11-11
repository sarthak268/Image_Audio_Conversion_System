from PIL import Image
import scipy.io.wavfile as wave
import numpy

audiofile = raw_input()
imagefile = raw_input()
samplingRate, audioChannels = wave.read(audiofile)

left = list(audioChannels[:, 0])
right = list(audioChannels[:, 1])


mleft = max(map(abs, left))
mright = max(map(abs, right))


def divide(a):
	return (a / float(mleft)) * min(mleft, 65535)

left = map(divide, left)

def divide(a):
	return (a / float(mright)) * min(mright, 65535)

right = map(divide, right)


im = Image.new("RGB", (936, 936), "black")


ai = 0
channel = 0
done = False
pixels = im.load()
for i in range(936):
	if done:
		break
	for j in range(936):
		if ai >= 437744:
			done = True
			break

		num = 0
		if channel == 0:
			num = left[ai]

		if channel == 1:
			num = right[ai]

		num = int(num)
		absnum = abs(num)
		numbinary = bin(absnum)[2:]
		numbinary = '0' * (16 - len(numbinary)) + numbinary
		leftpart = '0b' + numbinary[ : 8]
		rightpart = '0b' + numbinary[8 : ]
		r = int(leftpart, 2)
		g = int(rightpart, 2)
		if (num >= 0):
			b = 0
		else:
			b = 2

		pixels[i, j] = (r, g, b)


		if channel == 1:
			ai += 1

		channel = 1 - channel

im.save(imagefile)