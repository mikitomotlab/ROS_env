#!/usr/bin/env python
## coding: UTF-8

import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge, CvBridgeError
import socket
import SocketServer
import sys

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
        cv2.waitKey(1000)
       
        host = "192.168.11.18" #お使いのサーバーのホスト名を入れます
        #host = "192.168.2.7" #お使いのサーバーのホスト名を入れます
        port = 1245 #適当なPORTを指定してあげます

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #オブジェクトの作成をします
        print("preparing")

        client.connect((host, port)) #これでサーバーに接続します

        print("connecting")


        img_src = cv2.resize(cv_image,(480,270))

        #グレースケールに変換
        #im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        #print("OK")

        # jpegの圧縮率を設定 0～100値が高いほど高品質。何も指定しなければ95
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 100]

        # 文字列に変換
        jpegsByte = cv2.imencode('.jpeg', img_src, encode_param)[1].tostring()

        size = sys.getsizeof(jpegsByte)
        print(size)



        client.send(jpegsByte)
        print("finish sending image")

if __name__ == '__main__':
    rospy.init_node('color_extract')
    color = ColorExtract()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        pass
