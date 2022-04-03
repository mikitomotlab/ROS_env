#!/usr/bin/env python
## coding: UTF-8

import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge, CvBridgeError

class ColorExtract(object):
    def __init__(self):
        self._image_sub = rospy.Subscriber('/image', Image, self.callback)
        self._bridge = CvBridge()
        self._vel = Twist()


    def callback(self, data):
        #rospy.loginfo(rospy.get_name() + ' / I heard %s' , data.data)
        try:
            cv_image = self._bridge.imgmsg_to_cv2(data, 'bgr8')
        except CvBridgeError, e:
            print e

        cv2.imshow('cv_image' , cv_image)
        cv2.waitKey(0)

if __name__ == '__main__':
    rospy.init_node('color_extract')
    color = ColorExtract()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        pass
