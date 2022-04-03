#!/usr/bin/env python

from myrobot.srv import SetVelocity2
import rospy

def get(req):
    print req.linear_velocity

def server():
   rospy.init_node('setvel_server')
   s = rospy.Service('SetVelocity2', SetVelocity2, get)
   print "Ready to setvel"
   rospy.spin()


if __name__ == "__main__":
  server()
