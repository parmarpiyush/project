import cv2
from logger import log
import time

class yunet:

    def __init(self):
        self.height = 320
        self.width = 320

    def initialize(self, width, height):
        self.height = int(height)
        self.width = int(width)

    def face_detect(self, frame):
        model = cv2.FaceDetectorYN.create("face_detection_yunet_2023mar.onnx", "", (self.width, self.height))
        model.setInputSize((self.width, self.height))
        
        start = time.time()
        ret, faces = model.detect(frame)
        end = time.time()
        print(end-start)

        if ret and faces is not None:
            for face in faces:
                x, y, x_w, y_h = map(int, face[:4])
                cv2.rectangle(frame, (x, y), (x+x_w, y+y_h), (0, 255, 0), 2)
                #log.info(f"Face detected at: {x1}, {y1}, {x2}, {y2}")
                
        else:
            log.error("Face detection failed or no faces detected.")

        return frame

yunet = yunet()