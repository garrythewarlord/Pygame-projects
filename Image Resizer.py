from PIL import Image
import os


def resize_everything(x):
	the_length = len(get_file_names())
	the_filter = [int(e) for e in x.split('x')]
	for e in range(the_length):
		im = Image.open(get_file_names()[e])
		im = im.resize((the_filter[0], the_filter[1]))
		im.save("example{}.png".format(str(e)))

def get_file_names():
	the_list = []
	path = "C:\\Users\\idiot\\Desktop\\projects\\Image Resizer"
	for e in os.walk(path):
		for p in e:
			for c in p:
				if "jpg" in c or "png" in c:
					the_list.append(c)
	return the_list

def Image_Resizer():
	x = input("Would you like to resize everything? Y/N : ")
	if x == "Y" or x == "y":
		x = input("What size would you like to be? i.e 1x1 : ")
		resize_everything(x)
	else:
		for e in get_file_names():
			print(e)
		x = int(input("Which image would you like to resize? type 1 for image 1 etc. : ")) - 1
		im = Image.open(get_file_names()[x])
		x = input("What size would you like to be? i.e 1x1 : ")
		the_filter = [int(e) for e in x.split('x')]
		im = im.resize((the_filter[0], the_filter[1]))
		im.save("example.png")

Image_Resizer()
get_file_names()

	
