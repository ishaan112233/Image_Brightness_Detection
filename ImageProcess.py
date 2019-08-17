import cv2
import matplotlib.pyplot as plt
import argparse

arg = argparse.ArgumentParser()

arg.add_argument("-i","--image",required=True,help="Path to input image")

args = vars(arg.parse_args())

#For loading the image and normalize it.
def load_img():
	image = cv2.imread(args["image"])
	image = cv2.resize(image,(250,250))
	norm_img = cv2.normalize(image, None, alpha=0, beta=10,norm_type = cv2.NORM_MINMAX, dtype = cv2.CV_32F)
	return norm_img

#For Getting brightness of image: (0: low brightness level , 10: High Brightness Level)	
def get_brightness():
	img = load_img()
	lab = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
	l, a, b = cv2.split(lab)
	x, y, z = img.shape
	maxval = []
	#Accessing some part of Image
	count_percent = 10 #percent of total image
	count_percent = count_percent/100
	row_percent = int(count_percent*x) #1% of total pixels widthwise
	column_percent = int(count_percent*y) #1% of total pizel height wise
	for i in range(1,x-1):
			if i%row_percent == 0:
				for j in range(1, y-1):
					if j%column_percent == 0:
						pix_cord = (i,j)
						img_segment = l[i:i+10, j:j+10]
						(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(img_segment)
						maxval.append(maxVal)

	avg_maxval = round(sum(maxval) / len(maxval))
	print('Brightness: {}'.format(int(avg_maxval/10)))

if __name__ == '__main__':
	get_brightness()
