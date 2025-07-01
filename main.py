import cv2
import numpy as np
from logger import log
from yunet import yunet

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    log.error("Could not open camera or camera is not available on this system.")
    #TODO: Add a logger mechanism for readability
    print("Could not open camera or camera is not available on this system.")
    exit(1)

f_height = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
f_width = camera.get(cv2.CAP_PROP_FRAME_WIDTH)

log.info(f_height)
log.info(f_width)

yunet.initialize(f_width, f_height)

log.info("camera opened")
flag = True

while True:
    retVal, frame = camera.read()
    if not retVal:
        print("Failed to grab frame from camera.")
        break
    
    log.debug("frame read")
    #frame[:,:,0] = np.clip(frame[:,:,0] * 2 , 0 , 255)
    #time.sleep(1)
    # frame1 = (frame * 2) %255
    # frame2 = (frame * 0.5) % 255
    # cv2.imshow("screen1", frame1)
    # cv2.imshow("scree2", frame2)

    frame = yunet.face_detect(frame)
    cv2.imshow("screen", frame)
     
    if cv2.waitKey(33) & 0xFF == ord('q'):
        #playsound("alert.wav")
        print("exit")
        break
    
    # else:
    #     cv2.imshow("screen2", frame)  
    #time.sleep(3)
        
camera.release()
cv2.destroyAllWindows()



