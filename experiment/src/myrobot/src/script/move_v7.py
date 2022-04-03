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

xg = 0
yg = 0.1
zg = 0

def callback(data):
    x = rospy.loginfo(rospy.get_caller_id()+"I heard %s",data.pose[0].position.x)
    
    twist = Twist()
    twist.linear.x = 0.5
    twist.linear.y = 0.3
    twist.linear.z = 0
    twist.angular.x = 0
    twist.angular.y = 0
    twist.angular.z = 0

    state = ModelState()
    state.pose.position.x = xg 
    state.pose.position.y = yg
    state.pose.position.z = zg
    state.pose.orientation.x = 0
    state.pose.orientation.y = 0
    state.pose.orientation.z = 0
    pub = rospy.Publisher('/cmd_vel', Twist)
    #pub = rospy.Publisher('/gazebo/set_model_state', Twist)
    #pub = rospy.Publisher('/gazebo_msgs/Modelstate', Twist)
    #pub = rospy.Publisher('/gazebo/model_states', Twist,queue_size=10)
    pub.publish(twist)

    rospy.wait_for_service('gazebo/set_model_state')
    #set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
    set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
    resp = set_state( state )


    #msg = rospy.Publisher('/gazebo/set_model_state', SetModelState)
    #msg.publish(state)
    

def listener():
    rospy.init_node('node3')
    while True:
        try:
            sub = rospy.Subscriber('/gazebo/model_states', ModelStates, callback, queue_size=1)

        except :
            break
            pass
            sys.exit()

    #sub = rospy.Subscriber('/gazebo/get_model_state', ModelStates, callback, queue_size=1)
   #sub = rospy.Subscriber('/gazebo/get_model_state', GetModelState)
       # print(sub.pose[0].position.x)
   # rospy.loginfo("I head %s ",sub)
        #if xm==0 and ym==0 and zm==0 :
         #   break


if __name__ == '__main__':
    try:
        listener()
    except :
        pass
