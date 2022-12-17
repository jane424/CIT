import cv2
import time
import numpy as np
vc = cv2.VideoCapture(0)     

start = time.time()

#1(vc * cv2) = j
i = 0

while True :

 cur_time = time.time() - start

 print("time is " + str(cur_time))

 ret, frame = vc.read()
 cv2.putText(frame,"Picture", (50,100),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,4,(255,255,255),5) 
 
 frame = cv2.line(frame, (0,200),(640,200), (255,255,255),10)
 
 frame = cv2.circle(frame, (320,240), 10, (0,0,0),5)
 
 frame = cv2.rectangle(frame, (0,150),(480,0),(250,255,230),10)
 
 pts = np.array([[25,70],[25,160],[110,200],[200,160],[200,70],[110,20]],np.int32)
 pts = pts.reshape((-1,1,2))
 isClosed = True
 frame = cv2.polylines(frame, [pts], isClosed, (0,255,251), 5)
 
 cv2.imshow("video ", frame)


 if cv2.waitKey(1) & 0xFF == ord('s'):

  print("capturing")

  
  #for i in range(j):
  cv2.imwrite(str(i) +'image.jpg',frame)
  i = i+1
  if i > 10:
      i = 0
