from PIL import Image
import os
imgwidth={}

for img in os.listdir('./TEXTTIHANDWRITTEN/MYFONT/'):
	if img.endswith('.png'):
		char,ext=os.path.splitext(img)
		# print(char)
		pic=Image.open("./TEXTTIHANDWRITTEN/MYFONT/"+img)
		imgwidth[char]=pic.width;