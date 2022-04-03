import rospy
from std_msgs.msg import String
from gazebo_msgs.msg import ModelStates
from gazebo_msgs.srv import GetModelState
from geometry_msgs.msg import Twist


xg = 10
yg = 0
zg = 0

def listener():

    while True:
        rospy.init_node('node3')
    #sub = rospy.Subscriber('/gazebo/model_states', ModelStates, callback, queue_size=1)
    
        sub = rospy.Subscriber('/gazebo/model_states', ModelStates)
    #sub = rospy.Subscriber('/gazebo/get_model_state', ModelStates, callback, queue_size=1)
   #sub = rospy.Subscriber('/gazebo/get_model_state', GetModelState)
        print(sub)
   # rospy.loginfo("I head %s ",sub)
    
        x = sub.pose[0].position.x
        print x
        y = sub.pose[0].position.y
        z = sub.pose[0].position.z

        xm = xg - x
        ym = yg - y
        zm = zg - z
        twist = Twist()
        twist.liner.x = xm
        twist.liner.y = ym
        twist.liner.z = zm
    
        pub = rospy.publisher('/cmd_vel', Twist)
        pub.publish(twist)
   
        if (xm==0 and ym==0 and zm==0):
            break


if __name__ == '__main__':
    listener()
