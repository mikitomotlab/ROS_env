#!/usr/bin/env python
## coding: UTF-8

import sys 
sys.path.append('~/experiment/src/myrobot/srv/')
import rospy
import rospkg
import signal
from std_msgs.msg import String
from gazebo_msgs.msg import ModelStates
from gazebo_msgs.srv import GetModelState
from geometry_msgs.msg import Twist
from gazebo_msgs.msg import ModelState
from gazebo_msgs.srv import SetModelState
import time
import datetime
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
import csv
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import socket
import SocketServer
import sys
import time
#import SetVelocity
from myrobot.srv import SetVelocity2, SetVelocity2Response


#add camera capture
#change move_distance from integer to absolute value 
#adjust the coodinate of make_robot_camera5.launch
#add service

#xg = 1
#yg = 1
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)


class SendCapture:
    def __init__(self):
        #rospy.init_node('sendcapture')
        self._image_sub = rospy.Subscriber('/mybot/camera1/image_raw', Image, self.sendimg)
        self._bridge = CvBridge()
        self._vel = Twist()


    def sendimg(self, data):
        #rospy.loginfo(rospy.get_name() + ' / I heard %s' , data.data)
        start = time.time()
        try:
            cv_image = self._bridge.imgmsg_to_cv2(data, 'bgr8')
        except CvBridgeError, e:
            print e

        cv2.imshow('cv_image' , cv_image)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()
       
        host = "192.168.11.109" #お使いのサーバーのホスト名を入れます
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
        
        client.send(str(size))
        client.recv(1024)

        print(size)


        client.send(jpegsByte)
        print("finish sending image")
        msg = client.recv(1024)
        print(msg)
        elasped_time = time.time() - start
        print('RT :%.3f sec'% (elasped_time))
        
        return msg, elasped_time

def pose(gms):

    model_name = 'make_robot'
    name = 'ground_plane'

    resp1 = gms(model_name,name)
    x = resp1.pose.position.x
    y = resp1.pose.position.y
    rot_q = resp1.pose.orientation
    (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])
    return x, y, theta

def define_item(dx, dy, dth):
    print "in the define_item"
    dx_abs = abs(dx)
    dy_abs = abs(dy)
    dth_abs = abs(dth)
    xtime = cal_time(dx_abs)
    ytime = cal_time(dy_abs)
    thtime = cal_time(dth_abs)
   
   
    return xtime, ytime, thtime


def turn_right(qtime):
    #define 
    twist= Twist()
    twist.linear.x = 0.0
    twist.angular.z = 0.1

    #s = rospy.Service('cmd_vel', SetVelocity, pub_service)

    pub.publish(twist)
    start = time.time()
    m_time = time.time() -start
    x_vel = twist.linear.x
    print "check3"
    z_vel = twist.angular.z
    rooptime(start, m_time, qtime, x_vel, z_vel)
    #rooptime(start, m_time, qtime, twist.linear.x, twist.angular.z)
    stop()
    time.sleep(1)
    print "stop"
    

def turn_left(qtime):
    #define 
    twist= Twist()
    twist.linear.x = 0.0
    twist.angular.z = -0.1


    print "check"

    pub.publish(twist)
    print "check"
    start = time.time()
    m_time = time.time() -start
    print "check"
    x_vel = twist.linear.x
    print "check3"
    z_vel = twist.angular.z
    rooptime(start, m_time, qtime, x_vel, z_vel)
    print "check"
    stop()
    time.sleep(1)
    print "stop"


def forword(qtime):
    forword = Twist()
    forword.linear.x = 0.1
    forword.angular.z = 0.0
  
    print "qtime: {}".format(qtime)
    pub.publish(forword)
    start = time.time()
    m_time = time.time() -start
    rooptime(start, m_time, qtime, forword.linear.x, forword.angular.z)
    stop()
    time.sleep(1)

def back(qtime):
    back = Twist()
    back.linear.x = -0.1
    back.angular.z = 0.0
   
    #set_velocity = rospy.ServiceProxy('set_velocity2', SetVelocity2)
    #linear_vel = back.linear.x
    #angular_vel = back.angular.z
    #response = set_velocity(linear_vel, angular_vel)
   
    print "qtime: {}".format(qtime)
    pub.publish(back)
    start = time.time()
    m_time = time.time() -start
    #time.sleep(1)
    #time.sleep(5)
    #query = back.linear.x
    rooptime(start, m_time, qtime, back.linear.x, back.angular.z)
    print "forword"
    stop()
    time.sleep(3)

def stop():
    twist= Twist()
    twist.linear.x = 0.0
    twist.angular.z = 0.0
    pub.publish(twist)
    time.sleep(1)

def data_distance(xg, yg, thg, x, y, th):
    print "in the data_distance"
    dx = x - xg
    dy = y - yg
    dth = th - thg

    print "dx: {}, dy: {}".format(dx, dy)

    return dx, dy, dth


def cal_time(qt):
    qtime = qt * 10

    return qtime

def rooptime(start, m_time, qtime, x_vel, z_vel):
    print "check1"
    linear_vel = x_vel
    print "check3"
    angular_vel = z_vel
    print "check4"
    rospy.wait_for_service('SetVelocity2')
    try:
        vel = rospy.ServiceProxy('SetVelocity2', SetVelocity2)
        service = vel(linear_vel, angular_vel)
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e
    #if respose.success:
        #SetVelocity2= rospy.ServiceProxy('SetVelocity2', SetVelocity2)
        #print "check5"

    
    start = time.time()
    while m_time < qtime:
        print "m_time: {}".format(m_time)
        print "xtime: {}".format(qtime)
        s = rospy.Service('cmd_vel', SetVelocity, response)
        m_time = time.time() -start
        if m_time > qtime:
            print "break loop"
            break


def callback(xg, yg, thg, x, y, th):
    
    print "receive position !"
    dx, dy, dth = data_distance(xg, yg, thg, x, y, th)
    print "out of the datadistance"
    xtime, ytime, thtime = define_item(dx,dy,dth)

    print dx
    print "in the roop"
    time.sleep(1)
    c_time = 16
    if th >= 0 and 3.14 > th:

        th_0 = 3.14 - th
        th_0 = th_0 * 20
        print "in the roop"
        turn_right(th_0)
        print "look forword"
        stop()
        time.sleep(5)
        if dy > 0 and yg < 0: 
            turn_left(c_time)
            time.sleep(3)
            forword(ytime)
            time.sleep(3)
            turn_right(c_time +2)
            time.sleep(3)

        if dy > 0 and yg > 0:
            turn_left(c_time)
            time.sleep(3)
            forword(ytime)
            time.sleep(3)
            turn_right(c_time +2)
            time.sleep(3)

        if dy < 0 and yg < 0:
            turn_right(c_time)
            time.sleep(3)
            forword(ytime)
            time.sleep(3)
            turn_left(c_time +2)
            time.sleep(3)
        
        if dy < 0 and yg > 0:
            turn_right(c_time)
            time.sleep(3)
            forword(ytime)
            time.sleep(3)
            turn_left(c_time+2)
            time.sleep(3)
        
        if dx > 0 and xg < 0:
            forword(xtime)
            time.sleep(1)

        if dx > 0 and xg >0:
            forword(xtime)
            time.sleep(1)

        if dx < 0 and xg <0:
            forword(xtime)
            time.sleep(1)

        if dx < 0 and xg >0:
            forword(xtime)
            time.sleep(1)
        
        gms = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)

        x, y, th = pose(gms)
        dx, dy, dth = data_distance(xg, yg, thg, x, y, th)
        xtime, ytime, thtime = define_item(dx,dy,dth)
        th_time = th_time * 10

        if thg <0:
          turn_right(thtime)
          print "look forword"
          time.sleep(5)
        
        if thg <0:
          turn_left(thtime)
          print "look forword"
          time.sleep(5)
    
    if th >= -3.14 or th < 0 :
        th_0 = abs(-3.14 - th)
        print "th_0"
        th_0 = th_0 * 20
        turn_left(th_0)
        print "look forword"
        stop()
        print "look forword"
        time.sleep(5)

        if dy > 0 and yg < 0: 
            turn_left(c_time)
            time.sleep(3)
            forword(ytime)
            time.sleep(3)
            turn_right(c_time+2)
            time.sleep(3)

        if dy > 0 and yg > 0:
            turn_left(c_time)
            time.sleep(3)
            forword(ytime)
            time.sleep(3)
            turn_right(c_time+2)
            time.sleep(3)

        if dy < 0 and yg < 0:
            turn_right(c_time)
            time.sleep(3)
            forword(ytime)
            time.sleep(3)
            turn_left(c_time+2)
            time.sleep(3)
        
        if dy < 0 and yg > 0:
            turn_right(c_time)
            time.sleep(3)
            forword(ytime)
            time.sleep(3)
            turn_left(c_time+2)
            time.sleep(3)
        
        if dx > 0 and xg < 0:
            forword(xtime)
            time.sleep(1)

        if dx > 0 and xg >0:
            forword(xtime)
            time.sleep(1)

        if dx < 0 and xg <0:
            forword(xtime)
            time.sleep(1)

        if dx < 0 and xg >0:
            forword(xtime)
            time.sleep(1)
        
        gms = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)

        x, y, th = pose(gms)
        dx, dy, dth = data_distance(xg, yg, thg, x, y, th)
        xtime, ytime, thtime = define_item(dx,dy,dth)
        th_time = th_time * 10

        if thg <0:
          turn_right(thtime)
          print "look forword"
          time.sleep(5)
        
        if thg <0:
          turn_left(thtime)
          print "look forword"
          time.sleep(5)

    stop()
    print "x: {}, y: {}, theta: {}".format(x, y, th)
    time.sleep(5)
    dx, dy = check(xg, yg)
    check_point(dx, dy)

    #sys.exit()

def check(xg, yg):

    model_name = 'make_robot'
    name = 'ground_plane'

    try:
        gms = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
        resp1 = gms(model_name,name)
        x = resp1.pose.position.x
        y = resp1.pose.position.y
        rot_q = resp1.pose.orientation
        (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])

        print "x: {}, y: {}, theta: {}".format(x, y, th)
        time.sleep(5)
        
        dx = xg - x
        dy = yg - y
        print "dx: {}, dy: {}".format(dx, dy)
        id = datetime.datetime.today()

        with open('reserve1.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([id, x, y, theta, dx, dy])

        return dx, dy

        time.sleep(5)
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e
        time.sleep(5)

def check_point(dx, dy):
    print "in the check_point"

    time.sleep(5)
    if -0.1 < dx and dx< 0.1 and -0.1 < dy and dy < 0.1:
        print "stop !!"
        rospy.is_shutdown

    else:
        print "check"
        time.sleep(5)
        #listener()

def listener():
    rospy.init_node('node3', anonymous=True)
    #r = rospy.Rate(1)
    xg = input("x_goal:")
    yg = input("y_goal:")
    thg = input("th_goal:")

    print "check"
    #sub = rospy.Subscriber('/odom', Odometry, callback, queue_size=1)
    gms = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)

    x, y, theta = pose(gms)
    print "x: {}, y: {}, theta: {}".format(x, y, theta)
    print "xg: {}, yg: {}, thg: {}".format(xg, yg, thg)
    time.sleep(5)

    callback(xg, yg, thg, x, y, theta)

    print "1rooptime"
    #rospy.init_node('sendcapture')

    Capture = SendCapture()
    print "set constracter"
    #msg, time = Capture.sendimg()
    #print msg , time
    print "get msg"

    #r.sleep()
    #rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except :
        pass
        stop()
        rospy.is_shutdown
