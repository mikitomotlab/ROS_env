#!/usr/vin/env python

import rospy
from myrobot.srv import SetVelocity2
from geometry_msgs.msg import Twist

if __name__ == "__main__":
  twist = Twist()
  twist.linear.x = 0.1
  twist.angular.z = 0.0
  linear_vel = twist.linear.x
  angular_vel = twist.angular.z
  rospy.wait_for_service('SetVelocity2')
  try:
      vel = rospy.ServiceProxy('SetVelocity2', SetVelocity2)
      service = vel(linear_vel, angular_vel)

  except rospy.ServiceException, e:
      print "Service call failed: %s"%e
