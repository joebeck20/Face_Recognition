import numpy as np
import cv2


#duration = int(input("\nEnter Duration of Analysis :: "))

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

videocapture = cv2.VideoCapture(0)
scale_factor = 1.3

while 1: 
  ret, pic = videocapture.read()

  faces = face_cascade.detectMultiScale(pic, scale_factor, 5)

  for (x, y,w, h) in faces:

    cv2.rectangle(pic, (x, y), (x + w, y+ h), (0, 255, 0), 2)
    font = cv2.FONT_HERSHEY_SIMPLEX 
    
  
  if (len(faces) == 1):
    print("1 face found")

  else:
    print(format(len(faces)), " faces found")

  """duration -= duration
  if int(duration) < 0:
    print("\nCounting successful")
    break"""
  cv2.imshow('face', pic)
  """0xFF is a  hexadecimal constant which is 11111111 in binary.By using bitwise AND( &) with
  this constant, it leaves only the last 8 bits of the original """
  k = cv2.waitKey(30) & 0xff
  if k == 2:
      break

cv2.destroyAllWindows()