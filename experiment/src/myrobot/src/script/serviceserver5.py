#!/usr/bin/env python

from myrobot.srv import SetVelocity2, SetVelocity2Response
import rospy
import time

class pos:
    def __init__(self, th, dt, dth, dx, dy, st, sr):
        self.th = th
        self.dt = dt
        self.dth = dth
        self.dx = dx
        self.dy = dy
        self.start_t = st
        self.start_r = sr

    def get(self, req):
        print req.linear_velocity
        t_s = req.linear_velocity
        r_s = req.angular_velocity
        ltime = 0
        pi = 3.14
        if t_s != 0:
            if self.start_r != 0:
                self.start_t = time.time()
                finish = time.time()
                ltime = finish = self.start_r
                self.dth = r_s * ltime
                self.th = self.th + self.dth
                self.start_r = 0

            now = time.time()
            ftime = now - self.start_t

        if r_s != 0:
            if self.start_t != 0:
                self.start_r = time.time()
                finish = time.time()
                ltime = finish - self.start_t
                self.dt = t_s * ltime
                self.dx = self.dt * sin(self.th/pi)
                self.dy =self.dt * cos(self.th/pi)
                self.start_t = 0

            now = time.time()
            rtime = now - self.start_r

        linear_velocity = t_s
        angular_velocity = r_s
        print "th: {}".format(self.th)
        print "dx: {}".format(self.dx)
        print "dy: {}".format(self.dy)
        return SetVelocity2Response(linear_velocity, angular_velocity)
        #return SetVelocity2Response(success = is_set_success)

def zeroset():
    th = 0
    dt = 0
    dth = 0
    dx = 0
    dy = 0
    st = 0
    sr = 0
    print "Set Zero"
    return th, dt, dth, dx, dy, st, sr

def call_service(th, dt, dth, dx, dy, st, sr):
    d_pos = pos(th, dt, dth, dx, dy, st, sr)
    print "Ready to setvel"
    th = d_pos.th
    dt = d_pos.dt
    dth = d_pos.dth
    dx = d_pos.dx
    dy = d_pos.dy
    st = d_pos.start_t
    sr = d_pos.start_r
    return th, dt, dth, dx, dy, st, sr
    
def set_value(i):
    #global th, dt, dth, dx, dy, st, sr 
    if i == 0:
        th, dt, dth, dx, dy, st, sr = zeroset()
       
    th, dt, dth, dx, dy, st, sr = call_service(th, dt, dth, dx, dy, st, sr)
         
    i = i + 1
    return th, dt, dth, dx, dy, st, sr, i

def server(i):
    rospy.init_node('setvel_server')
    th, dt, dth, dx, dy, st, sr, i = set_value(i)
    d_pos = pos(th, dt, dth, dx, dy, st, sr)
    print "th: {}".format(d_pos.th)
    print "dx: {}".format(d_pos.dx)
    print "dy: {}".format(d_pos.dy)
    s = rospy.Service('SetVelocity2', SetVelocity2, d_pos.get)
    print "Ready to setvel"
    rospy.spin()


if __name__ == "__main__":
    i = 0
    global th, dt, dth, dx, dy, st, sr 
    server(i)

