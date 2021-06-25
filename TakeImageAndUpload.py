import cv2
import random
def takeImage():
    x = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result =  True
    while(result):
        ret,frame = videoCaptureObject.read()
        cv2.imwrite("NewPicture"+str (x) +".jpg",frame)
        result = False
    videoCaptureObject.release()
    cv2.destroyAllWindows()

takeImage()