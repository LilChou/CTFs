#! /usr/bin/env python
from PIL import Image

image1 = Image.open('image1.jpg')
image2 = Image.open('image2.jpg')

size = width, height = image1.size

new = Image.new('RGB', size)

img1 = image1.load()
img2 = image2.load()

data = new.load()

for x in range(width):
	for y in range(height):
		one = img1[x,y]
		two = img2[x,y]

		new_color = (one[0] ^ two[0],
					 one[1] ^ two[1],
					 one[2] ^ two[2])
		data[x,y] = new_color

new.save('new.jpg')
new.show()

