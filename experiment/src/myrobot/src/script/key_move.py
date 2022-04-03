#!/usr/bin/env python
 
import rospy
from geometry_msgs.msg import Twist
 
rospy.init_node('vel_publisher')
#pub = rospy.Publisher('/raspimouse/diff_drive_controller/cmd_vel', Twist, queue_size=10)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
while not rospy.is_shutdown():
    vel = Twist()
    direction = raw_input('w: forward, s: backward, a: left, d: right > ')
    if 'w' in direction:
        vel.linear.x = 0.5
    if 's' in direction:
        vel.linear.x = -0.5
    if 'a' in direction:
        vel.angular.z = 1.0
    if 'd' in direction:
        vel.angular.z = -1.0
    if 'q' in direction:
        break
    print vel
    pub.publish(vel)
