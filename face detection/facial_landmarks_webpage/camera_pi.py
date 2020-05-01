#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2014, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# Author : sosorry
# Date   : 05/31/2015
# Origin : http://blog.miguelgrinberg.com/post/video-streaming-with-flask

from imutils.video.pivideostream import PiVideoStream
from imutils import face_utils
import cv2
import numpy as np
import imutils
import dlib

detector_file = "model/haarcascade_frontalface_default.xml"
detector = cv2.CascadeClassifier(detector_file)

predictor_file = "model/shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(predictor_file)

class Camera(object):
    def __init__(self):
        if cv2.__version__.startswith('2'):
            PROP_FRAME_WIDTH = cv2.cv.CV_CAP_PROP_FRAME_WIDTH
            PROP_FRAME_HEIGHT = cv2.cv.CV_CAP_PROP_FRAME_HEIGHT
        elif cv2.__version__.startswith('3'):
            PROP_FRAME_WIDTH = cv2.CAP_PROP_FRAME_WIDTH
            PROP_FRAME_HEIGHT = cv2.CAP_PROP_FRAME_HEIGHT

        self.video = PiVideoStream().start()


    def __del__(self):
        self.video.release()
        

    def get_frame(self):
        
        while True:
            image = self.video.read()
            if image is not None:
                break

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # detect faces in the grayscale frame by opencv's method
        rects = detector.detectMultiScale(gray, scaleFactor=1.1, 
            minNeighbors=5, minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE)  

        # loop over the face detections
        face_counter = 0
        for (x, y, w, h) in rects:
            rect = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))

            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            (x, y, w, h) = face_utils.rect_to_bb(rect)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.putText(image, "Face #{}".format(face_counter + 1), (x - 10, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            for (x, y) in shape:
                cv2.circle(image, (x, y), 1, (0, 0, 255), -1)
            
            face_counter = face_counter + 1

        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tostring()
