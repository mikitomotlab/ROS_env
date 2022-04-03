import rospy
import rospkg
import sys
import signal
from std_msgs.msg import String
from gazebo_msgs.msg import ModelStates
from gazebo_msgs.srv import GetModelState
from geometry_msgs.msg import Twist
from gazebo_msgs.msg import ModelState
from gazebo_msgs.srv import SetModelState
import time
from nav_msgs.msg import Odometry

xg = 10
yg = 10
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

def turn_right():
    twist= Twist()
    twist.linear.x = 0.0
    twist.angular.z = 0.1
    start = time.time()
    LP = time.time() - start
    pub.publish(twist)
    LP = time.time() - start

def turn_left():
    twist= Twist()
    twist.linear.x = 0.0
    twist.angular.z = -0.1
    start = time.time()
    LT = time.time() - start
    while LT != 15 :
        pub.publish(twist)
        LT = time.time() - start
        if LT == 15:
            break

def forword():
    twist= Twist()
    twist.linear.x = 0.1
    twist.angular.z = 0.0
    print "check1"
    pub.publish(twist)
    print "finish"

def back(dT):
    twist= Twist()
    twist.linear.x = -0.1
    twist.angular.z = 0.0
    start = time.time()
    LT = time.time() - start
    pub.publish(twist)
    while LT == dT :
        #pub.publish(twist)
        LT = time.time() - start
def stop():
    twist= Twist()
    twist.linear.x = 0.0
    twist.angular.z = 0.0
    pub.publish(twist)
    time.sleep(5000)

def move_distance(data):
    
    #X = data.pose[0].position.x
    #Y = data.pose[0].position.x
    #Z = data.pose[0].position.x
    
    X = data.pose.pose.position.x
    Y = data.pose.pose.position.y
    Z = data.pose.pose.position.z
   
    dx = xg - X
    dy = yg - Y
    print X
    print "dx: {}, dy: {}".format(dx, dy)
    return dx, dy

def callback(data):
    
    print "receive position !"  
    dx, dy = move_distance(data) 
    print dx
    forword()

def listener():
    rospy.init_node('node3')
    sub = rospy.Subscriber('/odom', Odometry, callback, queue_size=1)
    print sub
    print "1roop"
    stop()
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except :
        pass
        rospy.is_shutdown
