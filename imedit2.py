import cv2 
import numpy as np

#quantize imaze/convert different grayscale level images(using KMEANS)
def quantizekmean(imgname):
	image = cv2.imread(imgname)
	gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	cv2.imwrite('GrayLenna.png',gray_image)

	#criteria
	img=cv2.imread('GrayLenna.png')
	Z=img.reshape((-1,3))
	Z = np.float32(Z)
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

	#quantize level
	K=int(input("Enter the quantize level : "))
	ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
	center = np.uint8(center)
	res = center[label.flatten()]
	quantimgkm = res.reshape((img.shape))
	cv2.imshow('quantimgkm',quantimgkm)
	cv2.imwrite('quantimgkm.jpg',quantimgkm)
	cv2.waitKey(3000)
	cv2.destroyAllWindows()

def addimg(imgname1,imgname2):
	def addcv(image_1, image_2):
		addImage = cv2.add(image_1, image_2)
		cv2.imwrite('addimopencv.jpg',addImage)
		cv2.imshow("addimopencv", addImage)
		cv2.waitKey(3000)
		cv2.destroyAllWindows()

	def addnum(image_1, image_2):
		img = image_1+image_2
		cv2.imwrite('addimnum.jpg',img)
		cv2.imshow('addimnum',img)
		cv2.waitKey(3000)
		cv2.destroyAllWindows()

	def addweigh(image_1, image_2):
		print("Alpha : Increasing alpha will bring background in concentration(0-1.0)")
		print("Gamma : Increasing gamma will bring foreground in concentration(0-1.0)")
		x=input("Enter alpha and beta : ").split()
		alpha=float(x[0])
		gamma=float(x[1])
		weightedSum = cv2.addWeighted(image_1, alpha, image_2, gamma, 0)
		cv2.imwrite('Weighted_Image.jpg',weightedSum)
		cv2.imshow('Weighted Image', weightedSum)	
		cv2.waitKey(3000)
		cv2.destroyAllWindows()

	image_1 = cv2.imread(imgname1)
	image_2 = cv2.imread(imgname2)
	print("===Add Images Method====")
	print("1.Images addition using opencv")
	print("2.Pixel by Pixel addition using numpy operation")
	print("3.Addition using addWeighted method")
	x=int(input("Enter the option : "))
	if(x==1):
		addcv(image_1, image_2)
	elif(x==2):
		addnum(image_1, image_2)
	elif(x==3):
		addweigh(image_1, image_2)
	else:
		print("Wrong option!!!")

def subimg(imgname1,imgname2):
	simg1 = cv2.imread(imgname1) 
	simg2 = cv2.imread(imgname2)
	simg1_gray = cv2.cvtColor(simg1, cv2.COLOR_BGR2GRAY)
	simg2_gray = cv2.cvtColor(simg2, cv2.COLOR_BGR2GRAY)
	sub = cv2.subtract(simg1_gray, simg2_gray)
	cv2.imshow('Subtracted image',sub)
	cv2.waitKey(3000)
	cv2.destroyAllWindows()
	x=int(input("Enter the threshold value(0-255) : "))
	ret, thresh = cv2.threshold(sub, x, 255, cv2.THRESH_BINARY)
	cv2.imwrite('threshold_img.jpg',thresh)
	cv2.imshow('threshold_img', thresh)
	cv2.waitKey(3000)
	cv2.destroyAllWindows()

def mulimg(imgname1,imgname2):
	img1 = cv2.imread(imgname1) 
	img2 = cv2.imread(imgname2)
	img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
	img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
	masked = cv2.bitwise_and(img2_gray, img1_gray, mask=None)
	cv2.imwrite('Masked_img.jpg',masked)
	cv2.imshow("Mask Applied to Image", masked)
	cv2.waitKey(3000)
	cv2.destroyAllWindows()

def mulimgc(imgname1,imgname2):
	board = cv2.imread(imgname1).astype(np.float32)
	shade = cv2.imread(imgname2).astype(np.float32)
	board_gray = cv2.cvtColor(board, cv2.COLOR_BGR2GRAY)
	shade_gray = cv2.cvtColor(shade, cv2.COLOR_BGR2GRAY)
	board_div = cv2.divide(board_gray, shade_gray)
	board_normalise = cv2.normalize(board_div, None, 0, 255, cv2.NORM_MINMAX)
	cv2.imwrite('imgclarity.jpg',board_normalise.astype(np.uint8))
	cv2.imshow('imgNormalize1', board_normalise.astype(np.uint8))
	cv2.waitKey(3000)
	cv2.destroyAllWindows()




