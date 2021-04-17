import numpy as np
import time
import cv2
from pygame import mixer

#function to play sound

def sound_play(total,sound):

	# Check if blue color object present in the ROI 	
	yes = (total) > Hatt_thickness[0]*Hatt_thickness[1]*0.8

	# If present play the respective instrument.
	if yes and sound==1:
		drum_clap.play()
		
	elif yes and sound==2:
		drum_snare.play()
		

#function to check the region of interest
def ROI_check(frame,sound):
	

	# converting the image into HSV to track blue color object 
	#In HSV, it is easier to represent a color than in BGR color-space. 
	# In our application, we will try to extract a blue colored object.
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	# generating mask for 
	mask = cv2.inRange(hsv, blueLower, blueUpper)
	
	# Calculating the nuber of white pixels depecting the blue color pixels in the ROI
	total = np.sum(mask)
	
	# Function that decides to play the instrument or not.
	sound_play(total,sound)

	
	return mask



# importing the audio files
mixer.init()
drum_clap = mixer.Sound('snare.wav')
drum_snare = mixer.Sound('hatt.wav')


# HSV range for detecting blue color 
blueLower = (100,150,50)
blueUpper = (140,255,255)

# Frame accusition from webcam/ usbcamera 
camera = cv2.VideoCapture(0)
ret,frame = camera.read()
H,W = frame.shape[:2]
fourcc = cv2.VideoWriter_fourcc(*'XVID')  
out = cv2.VideoWriter('output.avi',fourcc, 24.0, (640,480))  



# reading the image of hatt and snare for augmentation.
Hatt = cv2.resize(cv2.imread('./Images/Hatt.png'),(200,100),interpolation=cv2.INTER_CUBIC)
Snare = cv2.resize(cv2.imread('./Images/Snare.png'),(200,100),interpolation=cv2.INTER_CUBIC)


# Thickness of Instruments

Hatt_thickness = [200,100]


Snare_thickness = [200,100]





while True:
	
	# grab the current frame
	ret, frame = camera.read()
	frame = cv2.flip(frame,1)
	out.write(frame) 
	if not(ret):
		break
    
	# Selecting ROI corresponding to snare
	snare_ROI = np.copy(frame[310:410,380:580])
	mask = ROI_check(snare_ROI,1)
    
	# Selecting ROI corresponding to Hatt
	hatt_ROI = np.copy(frame[310:410,60:260])
	mask = ROI_check(hatt_ROI,2)

	# A writing text on an image.
	cv2.putText(frame,'ORIGIN 2021',(10,30),2,1,(20,20,20),2)
	
    
		# Augmenting the image of the instruments on the frame.
	frame[310:410,380:580] = cv2.addWeighted(Snare,1, frame[310:410,380:580],1, 0)
	frame[310:410,60:260] = cv2.addWeighted(Hatt,1, frame[310:410,60:260],1,0)
    

	cv2.imshow('Output',frame)
	key = cv2.waitKey(1) 
	# if the 'q' key is pressed, stop the loop
	if key == 27:
		break
	if key==112:
		cv2.waitKey(-1)
out.release()	
camera.release()
cv2.destroyAllWindows()