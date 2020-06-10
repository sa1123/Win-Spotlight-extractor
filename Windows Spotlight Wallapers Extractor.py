import os
import random
from PIL import Image
import shutil
import imagehash

def main():
	os.chdir('C:/Users/Sahil/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets')
	try:
		os.mkdir('C:/Users/Sahil/Pictures/Windows Spotlight Wallpapers')
	except:
		FileExistsError
	for f in os.listdir():
		im = Image.open(f)
		width = im.width
		if (width == 1920):
			shutil.copy(f,'C:/Users/Sahil/Pictures/Windows Spotlight Wallpapers')

def namefix():
	os.chdir('C:/Users/Sahil/Pictures/Windows Spotlight Wallpapers')
	for f in os.listdir():
		new_name = "wallpaper" + str(random.randint(1000,999999)) + ".jpg"
		os.rename(f, new_name)
	i=1
	for f in os.listdir():
		new_name = "wallpaper" + str(i) + ".jpg"
		os.rename(f, new_name)
		i+=1

def imhash():
	os.chdir('C:/Users/Sahil/Pictures/Windows Spotlight Wallpapers')
	hashlist = []
	for f in os.listdir():
		imghash = imagehash.average_hash(Image.open(f))
		if imghash not in hashlist:
			hashlist.append(imghash)
		else:
			os.remove(f)

if __name__ == '__main__':
	main()
	namefix()
	imhash()
