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
import datetime
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
import csv

#xg = 1
#yg = 1
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

def pose(gms):

    model_name = 'make_robot'
    name = 'ground_plane'

    resp1 = gms(model_name,name)
    x = resp1.pose.position.x
    y = resp1.pose.position.y
    rot_q = resp1.pose.orientation
    (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])
    return x, y, theta

def define_item(dx, dy):
    print "in the define_item"
    xtime = cal_time(dx)
    ytime = cal_time(dy)
   
    return xtime, ytime

def turn_right():
    #define 
    twist= Twist()
    twist.linear.x = 0.0
    twist.angular.z = 0.1

    pub.publish(twist)
    start = time.time()
    m_time = time.time() -start
    #time.sleep(1)
    rooptime(start, m_time, 16)
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
    #time.sleep(1)
    rooptime(start, m_time, 16)
    print "turn_right"
    stop()
    print "stop"


def forword(qtime):
    forword = Twist()
    forword.linear.x = 0.05
    forword.angular.z = 0.0
    print "qtime: {}".format(qtime)
    pub.publish(forword)
    start = time.time()
    m_time = time.time() -start
    #time.sleep(1)
    #time.sleep(5)
    rooptime(start, m_time, qtime)
    print "forword"
    time.sleep(1)
    stop()

def back(qtime):
    back = Twist()
    back.linear.x = -0.1
    back.angular.z = 0.0
    print "qtime: {}".format(qtime)
    pub.publish(back)
    start = time.time()
    m_time = time.time() -start
    #time.sleep(1)
    #time.sleep(5)
    rooptime(start, m_time, qtime)
    print "forword"
    time.sleep(3)

def stop():
    twist= Twist()
    twist.linear.x = 0.0
    twist.angular.z = 0.0
    pub.publish(twist)

def data_distance(xg, yg, x, y):
    print "in the data_distance"
    dx = xg - x
    dy = yg - y
    print "dx: {}, dy: {}".format(dx, dy)
    print "aaa check"

    return dx, dy


def cal_time(qt):
    qtime = qt * 20

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


def callback(xg, yg, x, y, theta):
    
    print "receive position !"
    dx, dy = data_distance(xg, yg, x, y)
    print "out of the datadistance"
    xtime, ytime = define_item(dx,dy)

    print dx
    print "in the roop"
    time.sleep(1)

    if dy > 0:
        turn_left()
        forword(ytime)
        turn_right()

    if dy < 0:
        turn_right()
        forword(ytime)
        turn_left()

    if dx >0:
        forword(xtime)

    if dx <0:
        back(xtime)

    stop()
    print "dx=0"

    dx, dy = check(xg, yg)
    check_point(dx, dy)

    #sys.exit()

def check(xg, yg):
    #rospy.init_node('check', anonymous=True)

    print "in the check"

    time.sleep(5)
    
    #rospy.Subscriber('/gazebo/model_states', geometry_msgs, check_point, queue_size=1)

    model_name = 'make_robot'
    name = 'ground_plane'

    try:
        gms = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
        resp1 = gms(model_name,name)
        x = resp1.pose.position.x
        y = resp1.pose.position.y
        rot_q = resp1.pose.orientation
        (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])
        print resp1.pose.position.x
        print "dx: {}, dy: {}, theta: {}".format(x, y, theta)

        dx = xg - x
        dy = yg - y
        print "dx: {}, dy: {}".format(dx, dy)
        id = datetime.datetime.today()

        with open('reserve1.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([id, x, y, theta, dx, dy])

        return dx, dy

        time.sleep(5)
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e
        time.sleep(5)

def check_point(dx, dy):
    print "in the check_point"

    time.sleep(5)
    if -0.1 < dx and dx< 0.1 and -0.1 < dy and dy < 0.1:
        print "stop !!"
        rospy.is_shutdown

    else:
        print "check"
        time.sleep(5)
        #listener()

def listener():
    rospy.init_node('node3', anonymous=True)
    #r = rospy.Rate(1)
    xg = input("x_goal:")
    yg = input("y_goal:")

    print "check"
    #sub = rospy.Subscriber('/odom', Odometry, callback, queue_size=1)
    gms = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)

    x, y, theta = pose(gms)
    print "x: {}, y: {}, theta: {}".format(x, y, theta)

    callback(xg, yg, x, y, theta)

    print "1rooptime"

    #r.sleep()
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except :
        pass
        stop()
        rospy.is_shutdown
