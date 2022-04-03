import rospy
import sys
from std_msgs.msg import String
from gazebo_msgs.msg import ModelStates
from gazebo_msgs.srv import GetModelState
from geometry_msgs.msg import Twist


xg = 0.5
yg = 0.1
zg = 0

def callback(data):
    x = rospy.loginfo(rospy.get_caller_id()+"I heard %s",data.pose[0].position.x)
    x = data.pose[0].position.x
    print x
    y = data.pose[0].position.y
    z = data.pose[0].position.z

    xm = xg - x
    ym = yg - y
    zm = zg - z
    print xm
    print ym
    print zm
    
    twist = Twist()
    twist.linear.x = xm
    twist.linear.y = ym
    twist.linear.z = zm

    #pub = rospy.Publisher('/cmd_vel', Twist)
    #pub = rospy.Publisher('/gazebo/set_model_state', Twist)
    pub = rospy.Publisher('/gazebo_msgs/Modelstate', Twist)
    pub.publish(twist)
    
    if xm==0 and ym==0 and zm==0 :
        sys.exit() 

def listener():
    while True:
        rospy.init_node('node3')
        sub = rospy.Subscriber('/gazebo/model_states', ModelStates, callback, queue_size=1)
    #sub = rospy.Subscriber('/gazebo/get_model_state', ModelStates, callback, queue_size=1)
   #sub = rospy.Subscriber('/gazebo/get_model_state', GetModelState)
       # print(sub.pose[0].position.x)
   # rospy.loginfo("I head %s ",sub)
        #if xm==0 and ym==0 and zm==0 :
         #   break


if __name__ == '__main__':
    try:
        listener()
    except KeyboardInterrupt:
        print "received c"
        sys.exit()
