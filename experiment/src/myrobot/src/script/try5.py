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
from tf.transformations import euler_from_quaternion

xg = 3
yg = 3
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

def define_item(data):
    dx, dy, theta = data_distance(data) 
    xtime = cal_time(dx)
    ytime = cal_time(dy)
    rot_q = data.pose.pose.orientation
    (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])
   
    return xtime, ytime

def turn_right():
    #define 
    twist= Twist()
    twist.linear.x = 0.0
    twist.angular.z = 0.1

    pub.publish(twist)
    start = time.time()
    m_time = time.time() -start
    time.sleep(1)
    rooptime(start, m_time, 15)
    print "turn_right"
    stop()
    print "stop"
    

def turn_left():
    #define 
    twist= Twist()
    twist.linear.x = 0.0
    twist.angular.z = -0.1

    pub.publish(twist)
    start = time.time()
    m_time = time.time() -start
    time.sleep(1)
    rooptime(start, m_time, 15)
    print "turn_right"
    stop()
    print "stop"


def forword(qtime):
    forword = Twist()
    forword.linear.x = 0.1
    forword.angular.z = 0.0
    print "qtime: {}".format(qtime)
    pub.publish(forword)
    start = time.time()
    m_time = time.time() -start
    time.sleep(1)
    #time.sleep(5)
    rooptime(start, m_time, qtime)
    print "forword"
    time.sleep(3)
    stop()

def back(qtime):
    back = Twist()
    back.linear.x = -0.1
    back.angular.z = 0.0
    print "qtime: {}".format(qtime)
    pub.publish(back)
    start = time.time()
    m_time = time.time() -start
    time.sleep(1)
    #time.sleep(5)
    rooptime(start, m_time, qtime)
    print "forword"
    time.sleep(3)

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
    rot_q = data.pose.pose.orientation
    (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])
   
    dx = xg - X
    dy = yg - Y
    print X
    print "dx: {}, dy: {}, theta:{}".format(dx, dy, theta)
    time.sleep(7)
    return dx, dy, theta

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


def cal_time(qt):
    qtime = qt * 10

    return qtime

def rooptime(start, m_time, qtime):
    start = time.time()
    while m_time < qtime:
        print "m_time: {}".format(m_time)
        print "xtime: {}".format(qtime)
        m_time = time.time() -start
        if m_time > qtime:
            print "break loop"
            break


def callback(data):
    
    print "receive position !"
    dx, dy, theta = data_distance(data)
    xtime, ytime = define_item(data)

    if dy > 0:
        turn_right()
        forword(ytime)
        turn_left()

    if dy < 0:
        turn_left()
        forword(ytime)
        turn_right()

    if dx >0:
        forword(xtime)

    if dx <0:
        back(xtime)

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
