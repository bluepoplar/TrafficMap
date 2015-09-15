import numpy as np
import cv2

def get_image(image_name):
	image = cv2.imread(image_name)

	# pre-process image. In my example, crop the black area and distant area of the image. 
	if image is not None:
		image = image[100:,:-20]
	return image

def find_cars(image,model):
	"""
	Use pre-trained cascade classifier to detect cars.
	"""
	car_cascade = cv2.CascadeClassifier(model)
	cars = car_cascade.detectMultiScale(image=image,scaleFactor=1.005,minNeighbors=8)
	return cars 

def highlight_cars(image,cars,color):
	"""
	Hightlight cars with rectangle.
	"""
	for (x,y,w,h) in cars:
		cv2.rectangle(image,(x,y),(x+w,y+h),color,2)

if __name__ == '__main__':
	images_name = 'images/image_%05d.jpg'
	max_images = 10
	for i in xrange(1,max_images):
		image_name = images_name % i
		image = get_image(image_name)
	
		if image is None:
			continue

		# cars3.xml is from: https://github.com/tomazas/opencv-lane-vehicle-track
		# another model I tested is harrout.xml. It is from: https://github.com/vbajpai/haartraining
		# comparing to the cars3.xml, it can recoginize cars better when cars are close, but have much hight false positive rate. 
		model = 'cars3.xml'
		cars = find_cars(image,model)
		print '[%s]%d cars are detected using model %s' % (image_name, len(cars),model)

		# show results in rectangle.
		highlight_cars(image,cars,(0,255,0))

		cv2.imshow('frame', image)
		cv2.waitKey(300)

	cv2.destroyAllWindows()