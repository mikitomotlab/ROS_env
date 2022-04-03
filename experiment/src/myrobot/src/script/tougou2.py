#!/usr/bin/env python
import rospy
from myrobot.msg import dpos
import time

def callback(message):
    print message.dx
    time.sleep(5)

if __name__ == "__main__":
    rospy.init_node('position')
    sub = rospy.Subscriber('dpos', dpos, callback)
    time.sleep(3)
    rospy.spin()
