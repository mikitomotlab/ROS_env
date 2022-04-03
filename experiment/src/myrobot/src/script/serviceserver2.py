#!/usr/bin/env python

from myrobot.srv import SetVelocity2, SetVelocityResponse
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


def get(req):
    d_pos = pos(th, dt, dth, dx, dy, st, sr)
    print req.linear_velocity
    t_s = req.linear_velocity
    r_s = req.angular_velocity
    ltime = 0
    pi = 3.14
    if t_s != 0:
        if d_pos.start_r != 0:
            d_pos.start_t = time.time()
            finish = time.time()
            ltime = finish = d_pos.start_r
            d_pos.dth = r_s * ltime
            d_pos.th = d_pos.th + d_pos.dth
            d_pos.start_r = 0

        now = time.time()
        ftime = now - d_pos.start_t

    if r_s != 0:
        if d_pos.start_t != 0:
            d_pos.start_r = time.time()
            finish = time.time()
            ltime = finish - d_pos.start_t
            d_pos.dt = t_s * ltime
            d_pos.dx = d_pos.dt * sin(d_pos.th/pi)
            d_pos.dy = d_pos.dt * cos(d_pos.th/pi)
            d_pos.start_t = 0

        now = time.time()
        rtime = now - d_pos.start_r

    linear_velocity = t_s
    angular_velocity = r_s
    #pub = rospy.Publisher('msg', Float64, queue_size=10)
    #pub.publish(msg)
    return SetVelocityResponse(linear_velocity, angular_velocity)
    

def server():
   print "Ready to setvel"
   rospy.init_node('setvel_server')
   print "Ready to setvel"
   th = 0
   dt = 0
   dth = 0
   dx = 0
   dy = 0
   st = 0
   sr = 0
   d_pos = pos(th, dt, dth, dx, dy, st, sr)
   print "Ready to setvel"
   while True:
       s = rospy.Service('SetVelocity2', SetVelocity2, get)
       th = d_pos.th
       dt = d_pos.dt
       dth = d_pos.dth
       dx = d_pos.dx
       dy = d_pos.dy
       st = d_pos.start_t
       sr = d_pos.start_r
       print "Ready to setvel"
       
   #rospy.spin()

if __name__ == "__main__":
    server()

