import cv2
import time

vc = cv2.VideoCapture(0)     

start = time.time()

#1(vc * cv2) = j
i = 0

while True :

 cur_time = time.time() - start

 print("time is " + str(cur_time))

 ret, frame = vc.read()
 cv2.putText(frame,"Picture", (50,100),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,4,(255,255,255),5) 
 cv2.imshow("video ", frame)
 
 if cv2.waitKey(1) & 0xFF == ord('s'):

  print("capturing")

  
  #for i in range(j):
  cv2.imwrite(str(i) +'image.jpg',frame)
  i = i+1
  if i > 10:
      i = 0
