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

xg = 0.5
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
    while LT == 15 :
        pub.publish(twist)
        LT = time.time() - start

def forword(r, dT):
    twist= Twist()
    twist.linear.x = 0.1
    twist.angular.z = 0.0
    start = time.time()
    LT = time.time() - start
    while LT == dT :
        pub.publish(twist)
        LT = time.time() - starti
        r.sleep()

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
def stop(r):
    twist= Twist()
    twist.linear.x = 0.0
    twist.angular.z = 0.0
    pub.publish(twist)
    r.sleep()

def move_distance(data):
    
    X = data.pose[0].position.x
    Y = data.pose[0].position.x
    Z = data.pose[0].position.x

    dx = xg - X
    dy = yg - Y
    return dx, dy

def callback(data):
    X = rospy.loginfo(rospy.get_caller_id()+"I heard %s",data.pose[0].position.x)
    Y = rospy.loginfo(rospy.get_caller_id()+"I heard %s",data.pose[0].position.y)
    Z = rospy.loginfo(rospy.get_caller_id()+"I heard %s",data.pose[0].position.z)
    print "receive position !"  
    r = rospy.Rate(10)  
    dx, dy = move_distance(data) 
    forword(r, dx) 
    stop(r)
    #Twist 
    #twist = Twist()
    #twist.linear.x = 0.5
    #twist.linear.y = 0.3
    #twist.linear.z = 0
    #twist.angular.x = 0
    #twist.angular.y = 0
    #twist.angular.z = 0

    #pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    #pub = rospy.Publisher('/gazebo/set_model_state', Twist)
    #pub = rospy.Publisher('/gazebo_msgs/Modelstate', Twist)
    #pub = rospy.Publisher('/gazebo/model_states', Twist,queue_size=10)
    
    #pub.publish(twist)

    #ModelState
    #state = ModelState()
    #state.pose.position.x = xg 
    #state.pose.position.y = yg
    #state.pose.position.z = zg
    #state.pose.orientation.x = 0
    #state.pose.orientation.y = 0
    #state.pose.orientation.z = 0
    #commmand = rospy.publisher('/gazebo/Modelstate', ModelState, queue_size=10)
    #command.publish(state)

    #else
    #rospy.wait_for_service('gazebo/set_model_state')
    #set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
    #set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
    #resp = set_state( state )


    #msg = rospy.Publisher('/gazebo/set_model_state', SetModelState)
    #msg.publish(state)

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
    while True:
        try:
            sub = rospy.Subscriber('/gazebo/model_states', ModelStates, callback, queue_size=1)

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
