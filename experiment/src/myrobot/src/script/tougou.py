#!/usr/bin/env python
## coding: UTF-8

from myrobot.srv import SetVelocity2, SetVelocity2Response
import rospy
import time
import math
from myrobot.srv import d_position, d_positionResponse
import numpy as np
from std_msgs.msg import Float64
from myrobot.msg import dpos

#dedreconing program

class pos:
#define structure pos value
    def __init__(self, dth, dx, dy, x, y, th):
        self.dth = dth
        self.dx = dx
        self.dy = dy
        self.x = x
        self.y = y
        self.th = th

#service callback and calculate moving distance
#define linear velocity: 0.1
#define angular velocity: 0.1
    def dedreconing(self, req):
        print req.dx
        self.dx = req.dx
        self.dy = req.dy
        self.dth = req.dth
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.th = self.th + self.dth
        return d_positionResponse(self.x, self.y, self.th)

    def sendserver(self):
        host = "192.168.11.109" #お使いのサーバーのホスト名を入れます
        #host = "192.168.2.7" #お使いのサーバーのホスト名を入れます
        port = 2028 #適当なPORTを指定してあげます

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #オブジェクトの作成をします
        print("preparing")

        client.connect((host, port)) #これでサーバーに接続します
        msg = [self.x, self.y, self.th]
        client.send(msg)
        

#define structure pos value
    def call_service(self, dth, dx, dy, x, y, th):
        dth = self.dth
        dx = self.dx
        dy = self.dy
        x = self.x
        y = self.y
        th = self.th
        return dth, dx, dy, x, y, th
    
#call service and go into get()
    def server(self, i):
        rospy.init_node('dpos')
        dth, dx, dy, x, y, th = self.call_service(self.dth, self.dx, self.dy, self.x, self.y, self.th)
        print "th: {}".format(self.th)
        print "dx: {}".format(self.dx)
        print "dy: {}".format(self.dy)
        s = rospy.Service('d_position', d_position, self.dedreconing)
        print "Ready to setvel"
        rospy.spin()

 
#set initial structre pos value   
def zeroset():
    dth = 0
    dx = 0
    dy = 0
    x = 0
    y = 0
    th = -3.14
    print "Set Zero"
    return dth, dx, dy, x, y, th

if __name__ == "__main__":
    i = 0
    global dth, dx, dy, x, y, th
    dth, dx, dy, x, y, th = zeroset()
    d_pos = pos(dth,dx, dy, x, y, th)
    time.sleep(3) 
    d_pos.server(i)

