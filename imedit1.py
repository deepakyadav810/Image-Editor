import cv2
from PIL import Image 
import PIL
from time import sleep

#conversion into grayscale
def grayscale(imgname):
	img = cv2.imread(imgname)
	gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	cv2.imshow('Grayscale', gray_image)
	cv2.waitKey(3000)
	cv2.destroyAllWindows()
	cv2.imwrite('gray_image.jpg',gray_image)

#quantize imaze/convert different grayscale images(using PIL)
def quantizeimg(imgname):
	img = Image.open(imgname)
	x=input("Enter the quantize level : ")
	im1 = img.quantize(x)
	imgGray = im1.convert('L')
	imgGray.save('quantimg.jpg')
	
#change dimension
def dimension(imgname):
	img = cv2.imread(imgname)
	# dimensions of current image
	dimensions = img.shape 
	# height, width, number of channels in image
	height = img.shape[0]
	width = img.shape[1]
	print('Image Dimension    : ',dimensions)
	print('Image Height       : ',height)
	print('Image Width        : ',width)
	x=input("Enter the new width and height : ").split()
	dim = (int(x[0]), int(x[1]))
	resized = cv2.resize(img, dim,interpolation = cv2.INTER_LINEAR)
	print('Resized Dimensions : ',resized.shape)
	cv2.imshow("Resized image", resized)
	cv2.waitKey(3000)
	cv2.destroyAllWindows()
	cv2.imwrite('resized.jpg',resized)
	


