#!/usr/bin/env python

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
    def __init__(self, th, dt, dth, dx, dy, x, y, st, sr):
        self.th = th
        self.dt = dt
        self.dth = dth
        self.dx = dx
        self.dy = dy
        self.x = x
        self.y = y
        self.start_b = sb
        self.start_n = sn

#service callback and calculate moving distance
#define linear velocity: 0.1
#define angular velocity: 0.1
    def get(self, req):
        print req.linear_velocity
        t_s = req.linear_velocity
        r_s = req.angular_velocity
        #ltime = 0
        pi = 3.14
        if r_s != 0:
            self.start_n = time.time()
            ltime = self.start_n - self.start_b
            print "ltime: {}".format(ltime)
            #time.sleep(2)
            self.dth = 0.1 * ltime
            self.th = self.th + self.dth / pi
            self.start_r = 0

        if t_s != 0:
            self.start_n = time.time()
            ltime = self.start_n - self.start_b
            self.dt = 0.1 * ltime
            self.dx = self.dx + self.dt * math.sin(self.th/pi)
            self.dy = self.dy + self.dt * math.cos(self.th/pi)
            self.start_t = 0


        linear_velocity = t_s
        angular_velocity = r_s

        self.x = self.x + self.dx
        self.y = self.y + self.dy

        print "th: {}".format(self.th)
        print "dx: {}".format(self.dx)
        print "dy: {}".format(self.dy)
        print "x: {}".format(self.x)
        print "y: {}".format(self.y)
        print "start_b: {}".format(self.start_b)
        print "start_n: {}".format(self.start_n)
        self.start_b = self.start_n
        #rospy.wait_for_service('d_position')
        #print "Waiting"
        #try:
        #    dpos = rospy.ServiceProxy('d_position', d_position)
        #    print "Waiting"
        #    res = dpos(self.dx, self.dy, self.dth)
        #    print res.x
            #time.sleep(2)
        #except rospy.ServiceException, e:
        #    print "service call failed: %s" %e

        pos = rospy.Publisher('dpos', dpos, queue_size=1)
        position = dpos()
        position.x = self.x
        position.y = self.y
        position.th = self.th
        pos.publish(position)
        return SetVelocity2Response(linear_velocity, angular_velocity)
        #return SetVelocity2Response(success = is_set_success)

#define structure pos value
    def call_service(self, th, dt, dth, dx, dy, x, y, st, sr):
        th = self.th
        dt = self.dt
        dth = self.dth
        dx = self.dx
        dy = self.dy
        x = self.x
        y = self.y
        sb = self.start_b
        sn = self.start_n
        #rospy.wait_for_service('d_position')
        #print "Waiting"
        #try:
        #    dpos = rospy.ServiceProxy('d_position', d_position)
        #    print "Waiting"
        #    res = dpos(dx, dy, dth)
        #    print res.x
        #    time.sleep(2)
        #except rospy.ServiceException, e:
        #    print "service call failed: %s" %e
        
        return th, dt, dth, dx, dy, x, y, sb, sn
    
#call service and go into get()
    def server(self, i):
        rospy.init_node('setvel_server')
        #th, dt, dth, dx, dy, st, sr, i = self.set_value(i)
        th, dt, dth, dx, dy, x, y, sb, sn = self.call_service(self.th, self.dt, self.dth, self.dx, self.dy, self.x, self.y, self.start_b, self.start_n)
        print "th: {}".format(self.th)
        print "dx: {}".format(self.dx)
        print "dy: {}".format(self.dy)
        s = rospy.Service('SetVelocity2', SetVelocity2, self.get)
        print "Ready to setvel"
        th, dt, dth, dx, dy, x, y, sb, sn = self.call_service(self.th, self.dt, self.dth, self.dx, self.dy, self.x, self.y, self.start_b, self.start_n)
        #rospy.wait_for_service('d_position')
        #print "Waiting"
        #try:
        #    dpos = rospy.ServiceProxy('d_position', d_position)
        #    print "Waiting"
        #    res = dpos(dx, dy, dth)
        #    print res.x
        #    time.sleep(2)
        #except rospy.ServiceException, e:
        #    print "service call failed: %s" %e
        
        
        rospy.spin()

# set structure pos value after 2roop
    def set_value(self, i):
        th, dt, dth, dx, dy, sb, sn = self.call_service(th, dt, dth, dx, dy, sb, sn)
         
        i = i + 1
        return th, dt, dth, dx, dy, sb, sn, i
 
#set initial structre pos value   
def zeroset():
    th = -180
    dt = 0
    dth = 0
    dx = 0
    dy = 0
    x = 0.0
    y = 0.0
    sb = time.time()
    sn = 0
    print "Set Zero"
    return th, dt, dth, dx, dy, x, y, sb, sn

if __name__ == "__main__":
    i = 0
    global th, dt, dth, dx, dy, x, y, sb, sn
    th, dt, dth, dx, dy, x, y, sb, sn = zeroset()
    d_pos = pos(th, dt, dth, dx, dy, x, y, sb, sn) 
    d_pos.server(i)

