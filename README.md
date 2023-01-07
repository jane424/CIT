# CIT
Webcam Project
Added: Yolo(You only look once), gui.py, PyQt5
------------------------------------------------------------------------------------------------------------------------------------------
To activate, you must first launch webcam and take a picture
*Note* In lines 38,39,40,41,42 (in webcam.py), hashtag lines 38 and 40 so the webcam can only make one picture: 0image.jpg
       If there are shapes and words, hashtag or remove the code otherwise the Yolo.py will not detect the picture behind

After launching the webcam, take a picture
*Note* The webcam will only be able to take one picture (named 0image.jpg)

After you have taken the picture, close the webcam and launch Yolo.py. After you do (it might take some time), a new file called 'image2.jpg'* will appear. This image has the detected images written on it.
*(you can change the name in line 47 in Yolo.py)
------------------------------------------------------------------------------------------------------------------------------------------
*Note* 'setting' folder is the quicker and least accurate version while 'setting2' folder is slower but more accurate

- if change 'setting' to 'setting2', change line 5,6,7
#net = cv2.dnn.readNet("setting/yolov4.weights", "setting/yolov4.cfg")
#classes = []
#with open("setting/coco.names", "r" as f:
(from Yolo.py) into
#net = cv2.dnn.readNet("setting2/yolov4.weights", "setting2/yolov4.cfg")
#classes = []
#with open("setting2/coco.names", "r" as f:
------------------------------------------------------------------------------------------------------------------------------------------
*Note* You can check what Yolo.py can detect in the file 'coco.names'
Here are some things that Yolo can detect:
person
bicycle
car
motorbike
aeroplane(airplane)
bus
train
truck
boat
traffic light
fire hydrant
stop sign
parking meter
bench
bird
cat
dog
horse
sheep
cow
elephant
bear
zebra
giraffe
backpack
umbrella
handbag
tie
suitcase
frisbee
skis
snowboard
sportsball
etc.
------------------------------------------------------------------------------------------------------------------------------------------
'gui.py' is the pyqt code.
*Notes*
import sys ----> sys is to control the Python interpreter
import os -----> os is to control the operating system

from PyQt5.QtWidgets import * ----------> From a import * : imports all elements of a
from PyQt5 import uic
UI = 'webcam.ui' ----------> UI = ‘ui name created in the previous data’ can be imported as an object.

class Dialog(QDialog): --------> Creating a class called Dialog
 def __init__(self):   --------> 'init' is a functon used when assigning a class
    	super().__init__() ------>
    	uic.loadUi(UI, self)
    	self.setting()

------------------------------------------------------------------------------------------------------------------------------------------
Next time, I want to find a way to make the detection much more accurate.
