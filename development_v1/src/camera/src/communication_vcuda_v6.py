#! /usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import SocketServer
import socket
import datetime
import glob
import cv2
import sys
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

#!/usr/bin/env python
"""OpenCV feature detectors with ros CompressedImage Topics in python.

This example subscribes to a ros topic containing sensor_msgs 
CompressedImage. It converts the CompressedImage into a numpy.ndarray, 
then detects and marks features in that image. It finally displays 
and publishes the new image - again as CompressedImage topic.
"""
# Python libs
import sys, time

# numpy and scipy
import numpy as np
#from scipy.ndimage import filters

# OpenCV
#import cv2

# Ros libraries
import roslib
import rospy

# Ros Messages
from sensor_msgs.msg import CompressedImage
# We do not use cv_bridge it does not support CompressedImage in python
# from cv_bridge import CvBridge, CvBridgeError

VERBOSE=False

#class image_feature:

    #def __init__(self):
        #'''Initialize ros publisher, ros subscriber'''

        # subscribed Topic
        #self.subscriber = rospy.Subscriber('/image_topic', Image, self.callback,  queue_size = 1)
        #if VERBOSE :


            #print "subscribed to /camera/image/compressed"

def Capture():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
      print("cannot open camera")

    ret, frame = cap.read()
    cv2.imshow('try', frame)
    cv2.imwrite('/home/miki/development_v1/src/camera/src/images/image.png', frame)
    cv2.waitKey(1000)
    return(frame)




def callback(image_np):
    #'''Callback function of subscribed topic. 
    #Here images get converted and features detected'''
    #if VERBOSE :
        #print 'received image of type: "%s"' % ros_data.format

    #rospy.on_shutdown(listener)

    #### direct conversion to CV2 ####
    #image_np = np.fromstring(ros_data, np.uint8)
    #image_np = cv2.imdecode(image_np, cv2.CV_LOAD_IMAGE_COLOR)
    #image_np = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

    #cv2.imshow("try1", image_np)
    #cv2.waitKey(2000)
        
    host = "192.168.11.180"
    port = 12345
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #???????????????????????????????????????
    client.connect((host, port)) #???????????????????????????????????????

    date = datetime.datetime.today()
    date =date.strftime('%y%m%d%H%M%S')

    myname = 'raspi7'
    date = str(date)
    date += myname

    client.send (date)

    msg = client.recv(1024)

    print (msg)

    #cv2.imshow("try1", image_np)
    #cv2.waitKey(2000)

    img_src = cv2.resize(image_np, (480, 270))

    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

    imbyte = cv2.imencode('.jpeg', img_src, encode_param)[1].tostring()

    size = sys.getsizeof(imbyte)
    size = str(size)
    client.send(size)
    #print (size)
    a = client.recv(1024)
    print (a)
    client.send(imbyte)
    #b = client.recv(1024)
    #print (b)
    client.shutdown(1)
    client.close()

 

#def main(args):
    #print("waiting image data")
    #rospy.init_node('listener', anonymous=True)
    #subscriber = rospy.Subscriber("/image_topic", Image, callback)
    #print("get image")
    #ic = image_feature()
    #rospy.init_node('image_feature', anonymous=True)
    #try:
        #rospy.spin()
    #except KeyboardInterrupt:
        #print "Shutting down ROS Image feature detector module"
    #cv2.destroyAllWindows()

if __name__ == '__main__':
    
    date = datetime.datetime.now()
    #date =date.strftime('%y%m%d%H%M%S')
    print(date)
    image = Capture()
    callback(image)
