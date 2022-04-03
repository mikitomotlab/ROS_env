import rospy
import sys
from std_msgs.msg import String
from gazebo_msgs.msg import ModelStates
from gazebo_msgs.srv import GetModelState
from geometry_msgs.msg import Twist


xg = 20
yg = 0.1
zg = 0

def callback(data):
    x = rospy.loginfo(rospy.get_caller_id()+"I heard %s",data.pose[0].position.x)
    
    twist = Twist()
    twist.linear.x = xg
    twist.linear.y = yg
    twist.linear.z = zg
    twist.angular.x = 0
    twist.angular.y = 0
    twist.angular.z = 0

    pose = Pose()
    pose.position.x = xg 
    pose.position.y = yg
    pose.position.z = zg
    #pub = rospy.Publisher('/cmd_vel', Twist)
    #pub = rospy.Publisher('/gazebo/set_model_state', Twist)
    pub = rospy.Publisher('/gazebo_msgs/Modelstate', Twist)
    #pub = rospy.Publisher('/gazebo/model_states', Twist,queue_size=10)
    pub.publish(pose)

    msg = rospy.Publisher('/gazebo/set_model_state', Twist)
    msg.publish(twist)
    

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
