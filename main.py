from imedit1 import *
from imedit2 import *

x=True
while(x!=False):
	print("=========Menu==========")
	print("1.Convert image into grayscale")
	print("2.Quantize image using PIL")
	print("3.Change Dimension of image")
	print("4.Quantize image using KMEANS")
	print("5.Adding two images")
	print("6.Threshold images")
	print("7.Image spotting using Multiplication")
	print("8.Image clarity using Multiplication")
	inp=int(input("Enter the option : "))
	if(inp==1):
		imgname=input("Enter the image file name : ")
		grayscale(imgname)
	elif(inp==2):
		imgname=input("Enter the image file name : ")
		quantizeimg(imgname)
	elif(inp==3):
		imgname=input("Enter the image file name : ")
		dimension(imgname)
	elif(inp==4):
		imgname=input("Enter the image file name : ")
		quantizekmean(imgname)
	elif(inp==5):
		imgname=input("Enter two image file names  : ").split()
		addimg(imgname[0],imgname[1])
	elif(inp==6):
		imgname=input("Enter two image file names  : ").split()
		subimg(imgname[0],imgname[1])
	elif(inp==7):
		imgname=input("Enter two image file names  : ").split()
		mulimg(imgname[0],imgname[1])
	elif(inp==8):
		imgname=input("Enter two image file names  : ").split()
		mulimgc(imgname[0],imgname[1])
	elif(inp==9):
		x=False
	else:
		print("Wrong Option!!!")
	
