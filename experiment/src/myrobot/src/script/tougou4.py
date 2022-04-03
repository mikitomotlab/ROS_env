#!/usr/bin/env python
## coding: UTF-8
import rospy
from myrobot.msg import dpos
import time
from gazebo_msgs.msg import ModelStates
from gazebo_msgs.srv import GetModelStates
import datetime
import csv
import cv2
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
import socket
import SocketServer
import sys
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist

#カメラ撮影ができるようにした

def check():
    
    #gms = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
    #x, y, theta = pose(gms)

    model_name = 'make_robot'
    name = 'ground_plane'

    try:
        gms = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
        resp1 = gms(model_name,name)
        x = resp1.pose.position.x
        y = resp1.pose.position.y
        rot_q = resp1.pose.orientation
        (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])

        #print "x: {}, y: {}, theta: {}".format(x, y, th)
        #time.sleep(5)
        
        #id = datetime.datetime.today()

        #with open('reserve1.csv', 'a') as f:
        #    writer = csv.writer(f)
        #    writer.writerow([id, x, y, theta, dx, dy])
    
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e
    
    return x, y, theta


class SendCapture:
    def __init__(self, x, y, th):
        #rospy.init_node('sendcapture')
        self._image_sub = rospy.Subscriber('/mybot/camera1/image_raw', Image, self.sendimg)
        self._bridge = CvBridge()
        self._vel = Twist()
        self.x = x
        self.y = y
        self.th = th


    def sendimg(self, data):
        #rospy.loginfo(rospy.get_name() + ' / I heard %s' , data.data)
        start = time.time()
        try:
            cv_image = self._bridge.imgmsg_to_cv2(data, 'bgr8')
        except CvBridgeError, e:
            print e

        #cv2.imshow('cv_image' , cv_image)
        #cv2.waitKey(1000)
        #cv2.destroyAllWindows()

       #真値の位置を受け取る 
        x_r, y_r, th_r = check()
       
        host = "192.168.11.110" #お使いのサーバーのホスト名を入れます
        #host = "192.168.2.7" #お使いのサーバーのホスト名を入れます
        port = 1245 #適当なPORTを指定してあげます

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #オブジェクトの作成をします
        client.connect((host, port)) #これでサーバーに接続します

        img_src = cv2.resize(cv_image,(480,270))

        #グレースケールに変換
        #im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        #print("OK")

        # jpegの圧縮率を設定 0～100値が高いほど高品質。何も指定しなければ95
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 100]

        # 文字列に変換
        jpegsByte = cv2.imencode('.jpeg', img_src, encode_param)[1].tostring()

        size = sys.getsizeof(jpegsByte)
        client.send(str(size))
        msg1 = client.recv(1024)
        print msg1

        client.send(jpegsByte)
        print("finish sending image")
        msg = client.recv(1024)
        print(msg)
        
        id = datetime.datetime.today()

        with open('reserve1.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([id, x_r, y_r, th_r, self.x, self.y, self.th])
    
        
        return msg

def callback(message):
    print message.x
    Capture = SendCapture(message.x, message.y, message.th)
    time.sleep(5)

if __name__ == "__main__":
    rospy.init_node('position')
    sub = rospy.Subscriber('dpos', dpos, callback)
    time.sleep(3)
    rospy.spin()
