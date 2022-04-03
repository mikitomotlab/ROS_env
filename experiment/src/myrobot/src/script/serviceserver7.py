#!/usr/bin/env python

from myrobot.srv import SetVelocity2, SetVelocity2Response
import rospy
import time
import math
from myrobot.srv import d_position
import numpy as np
from std_msgs.msg import Float64

#dedreconing program

class pos:
#define structure pos value
    def __init__(self, th, dt, dth, dx, dy, st, sr):
        self.th = th
        self.dt = dt
        self.dth = dth
        self.dx = dx
        self.dy = dy
        self.start_t = st
        self.start_r = sr

#service callback and calculate moving distance
#define linear velocity: 0.1
#define angular velocity: 0.1
    def get(self, req):
        print req.linear_velocity
        t_s = req.linear_velocity
        r_s = req.angular_velocity
        #ltime = 0
        pi = 3.14
        if t_s != 0:
            if self.start_r != 0:
                self.start_t = time.time()
                finish = time.time()
                ltime = finish - self.start_r
                print "finish: {}".format(finish)
                print "ltime: {}".format(ltime)
                #time.sleep(2)
                self.dth = 0.1 * ltime
                self.th = self.th + self.dth / pi
                self.start_r = 0

            now = time.time()
            ftime = now - self.start_t
            print "ftime: {}".format(ftime)

        if r_s != 0:
            if self.start_t != 0:
                self.start_r = time.time()
                finish = time.time()
                ltime = finish - self.start_t
                self.dt = 0.1 * ltime
                self.dx = self.dt * math.sin(self.th/pi)
                self.dy = self.dt * math.cos(self.th/pi)
                self.start_t = 0

            now = time.time()
            rtime = now - self.start_r
            print "rtime: {}".format(rtime)

        linear_velocity = t_s
        angular_velocity = r_s
        print "th: {}".format(self.th)
        print "dx: {}".format(self.dx)
        print "dy: {}".format(self.dy)
        print "start_t: {}".format(self.start_t)
        print "start_r: {}".format(self.start_r)
        return SetVelocity2Response(linear_velocity, angular_velocity)
        #return SetVelocity2Response(success = is_set_success)

#define structure pos value
    def call_service(self, th, dt, dth, dx, dy, st, sr):
        th = self.th
        dt = self.dt
        dth = self.dth
        dx = self.dx
        dy = self.dy
        st = self.start_t
        sr = self.start_r
        return th, dt, dth, dx, dy, st, sr
    
#call service and go into get()
    def server(self, i):
        rospy.init_node('setvel_server')
        #th, dt, dth, dx, dy, st, sr, i = self.set_value(i)
        th, dt, dth, dx, dy, st, sr = self.call_service(self.th, self.dt, self.dth, self.dx, self.dy, self.start_t, self.start_r)
        print "th: {}".format(d_pos.th)
        print "dx: {}".format(d_pos.dx)
        print "dy: {}".format(d_pos.dy)
        s = rospy.Service('SetVelocity2', SetVelocity2, d_pos.get)
        print "Ready to setvel"
        print "Ready to setvel"
        #msg = np.array([d_pos.th, d_pos.dx, d_pos,dy], dtype=np.float64)
        #msg = np.array([d_pos.th, d_pos.dx, d_pos,dy])
       # msg = np.array([0, 0.1, 0.1])
        #msg = rospy.get_time()
        pub = rospy.Publisher('dpos', dpos, queue_size=1)
        msg = dpos()
        #msg.msg = np.array([self.th, self.dx, self,dy])
        msg.dx = self.dx
        msg.dy = self.dy
        msg.dth = self.dth
        pub.publish(msg)
        rospy.spin()

# set structure pos value after 2roop
    def set_value(self, i):
        th, dt, dth, dx, dy, st, sr = self.call_service(th, dt, dth, dx, dy, st, sr)
         
        i = i + 1
        return th, dt, dth, dx, dy, st, sr, i
 
#set initial structre pos value   
def zeroset():
    th = -3.14
    dt = 0
    dth = 0
    dx = 0
    dy = 0
    st = 0
    sr = time.time()
    print "Set Zero"
    return th, dt, dth, dx, dy, st, sr

if __name__ == "__main__":
    i = 0
    global th, dt, dth, dx, dy, st, sr
    th, dt, dth, dx, dy, st, sr = zeroset()
    d_pos = pos(th, dt, dth,dx, dy, st, sr) 
    d_pos.server(i)

