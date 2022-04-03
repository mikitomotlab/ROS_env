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

xg = 3
yg = 3
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

def turn_right(data):
    twist= Twist()
    twist.linear.x = 0.0
    twist.angular.z = 0.1
    start = time.time()
    pub.publish(twist)
    time.sleep(1)
    LP = time.time() - start
    dx, dy = data_distance(data) 
    xtime, ytime = cal_time(dx, dy)
    start = time.time()
    m_time = time.time() -start
    rooptime(start, m_time, 15)
    print "turn_right"
    stop()
    print "stop"
    forword(dx, dy)
    time.sleep(3)
    print "forword"
    rooptime(start, m_time, ytime)
    

def turn_left(data):
    twist= Twist()
    twist.linear.x = 0.0
    twist.angular.z = -0.1
    start = time.time()
    pub.publish(twist)
    dx, dy = data_distance(data) 
    xtime, ytime = cal_time(dx, dy)
    start = time.time()
    m_time = time.time() -start
    rooptime(start, m_time, 15)
    stop()
    forword(data)
    rooptime(start, m_time, ytime)

def forword(dx,dy):
    forword = Twist()
    forword.linear.x = 0.1
    forword.angular.z = 0.0
    print "check1"
    pub.publish(forword)
    print "finish"
    time.sleep(1)
    xtime, ytime = cal_time(dx, dy)
    start = time.time()
    m_time = time.time() -start
    print "xtime: {}".format(xtime)
    time.sleep(5)
    rooptime(start, m_time, xtime)
    print "forword"
    time.sleep(3)
    stop()

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

def data_distance(data):
    
    #X = data.pose[0].position.x
    
    X = data.pose.pose.position.x
    Y = data.pose.pose.position.y
    Z = data.pose.pose.position.z
   
    dx = xg - X
    dy = yg - Y
    print X
    print "dx: {}, dy: {}".format(dx, dy)
    return dx, dy
    
def get_position():
    sub = rospy.Subscriber('/odom', Odometry,move_distance, queue_size=1)
    return sub

def move_distance(data):
    
    #data = get_position() 
    X = data.pose.pose.position.x
    Y = data.pose.pose.position.y
    Z = data.pose.pose.position.z
   
    dx = xg - X
    dy = yg - Y
    print X
    print "dx: {}, dy: {}".format(dx, dy)
    return dx, dy


def cal_time(dx, dy):
    xtime = dx * 10
    ytime = dy * 10

    return xtime, ytime

def rooptime(start, m_time, xtime):
    while m_time < xtime:
        print "m_time: {}".format(m_time)
        print "xtime: {}".format(xtime)
        m_time = time.time() -start
        if m_time > xtime:
            print "break loop"
            break

    print "loop"

def callback(data):
    
    print "receive position !"  
    dx, dy = data_distance(data) 
    print dx
    xtime, ytime = cal_time(dx, dy)
    start = time.time()
    m_time = time.time() -start

    if dy > 0:
        turn_right(data)
        #turn_left(data)
    if dx >0:
        forword(data)

    stop()
    print "dx=0"

def listener():
    rospy.init_node('node3', anonymous=True)
    sub = rospy.Subscriber('/odom', Odometry, callback, queue_size=1)
    print "1roop"
    #stop()
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except :
        pass
        stop()
        rospy.is_shutdown
