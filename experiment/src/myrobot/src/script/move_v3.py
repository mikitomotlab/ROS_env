import rospy
from std_msgs.msg import String
from gazebo_msgs.msg import ModelStates
from gazebo_msgs.srv import GetModelState


xg = 10
yg = 0
zg = 0

def callback(data):
    x = rospy.loginfo(rospy.get_caller_id()+"I heard %s",data.pose[0].position.x)
    x = data.pose[0].position.x
    print x
    y = data.pose[0].position.y
    z = data.pose[0].position.z

#ifで分岐をする
    xm = xg - x
    ym = yg - y
    zm = zg - z

def listener():
    rospy.init_node('node3')
    sub = rospy.Subscriber('/gazebo/model_states', ModelStates, callback, queue_size=1)
    #sub = rospy.Subscriber('/gazebo/get_model_state', ModelStates, callback, queue_size=1)
   #sub = rospy.Subscriber('/gazebo/get_model_state', GetModelState)
    print(sub)
   # rospy.loginfo("I head %s ",sub)

if __name__ == '__main__':
    listener()
