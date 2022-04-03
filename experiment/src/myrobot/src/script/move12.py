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

xg = 100
yg = 0.1
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

def turn_right():
    twist= Twist()
    twist.linear.x = 0.0
    twist.angular.z = 0.1
    start = time.time()
    LP = time.time() - start
    while LP == 15 :
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

def move_distance(data):
    
    X = data.pose[0].position.x
    Y = data.pose[0].position.x
    Z = data.pose[0].position.x

    dx = xg - X
    dy = yg - Y
    return dx, dy

def callback(data):
    
    print "receive position !"  
    r = rospy.Rate(10)  
    dx, dy = move_distance(data) 
    print dx
    start = time.time()
    LT = time.time() - start
    forword()
    print "check"
    time.sleep(LT)
    print "sleep"
    #while dx != LT : 
        #forword()
        #time.sleep(1000)
        #print "loop" 
        #LT = time.time() - start
       # print type(dx)
        #print type(LT)
        #print "LT="+str(LT)
       # print "dx="+str(dx)

    print "out of loop"   
   # stop(r)
    print "check3"

"""
    
    while xg==X and yg==Y :
        if dx < 0 :
            dx, dy = move_distance(data)
            back(dx)
            stop()
        if dx > 0:
            dx, dy = move_distance(data)
            forword(dx)
            stop()
        if dy < 0:
            dx, dy = move_distance(data)
            turn_right()
            forword(dy)
            stop()
        if dy > 0:
            dx, dy = move_distance(data)
            turn_left()
            forword(dy)
            stop()


"""
    #stop()
    #sys.exit()

    

def listener():
    rospy.init_node('node3')
    try:
        while True:
            sub = rospy.Subscriber('/gazebo/model_states', ModelStates, callback, queue_size=1)
            time.sleep(1000)
            print "1roop"
            stop()

    except :
        print("stopping")
        rospy.is_shutdown()
        pass
        sys.exit()

if __name__ == '__main__':
    try:
        listener()
    except :
        pass
        rospy.is_shutdown
