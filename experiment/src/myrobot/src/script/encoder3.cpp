#include <ros/ros.h>  // rosで必要はヘッダーファイル
#include <geometry_msgs/Twist.h> // ロボットを動かすために必要
#include <nav_msgs/Odometry.h>
#include <tf/transform_broadcaster.h>
#include <tf/transform_datatypes.h>
#include <gazebo_msgs/ModelStates.h> 
#include <sensor_msgs/JointState.h>

using namespace std;

// /gazebo/model_statesトピックから真の位置Pos(x,y,z)と姿勢Pose(roll, pitch ,yaw)を表示
void cbModelStates(const gazebo_msgs::ModelStates::ConstPtr& msg)
{
  ROS_INFO("Real Pos (x:%f, y:%f, z:%f)", msg->pose[1].position.x,msg->pose[1].position.y, msg->pose[1].position.z);

    tf::Quaternion q(msg->pose[1].orientation.x, msg->pose[1].orientation.y, msg->pose[1].orientation.z, msg->pose[1].orientation.w);  
    // tf::Quaternion q(quat.x, quat.y, quat.z, quat.w);
    tf::Matrix3x3 m(q);
    double roll, pitch, yaw;
    m.getRPY(roll, pitch, yaw);

    ROS_INFO("Real Pose (roll:%f, pitch:%f, yaw:%f) ", roll, pitch, yaw);
}

// 参考：Turtlebot3の車輪直径0.066 [m]
void cbMyOdom(const sensor_msgs::JointState::ConstPtr& jointstate)
{

    double wheel_r_vel = jointstate->velocity[0]; // 右車軸の位置[rad]
    double wheel_l_vel  = jointstate->velocity[1]; // 左車軸の位置[rad]

    double wheel_right_joint_pos = jointstate->position[0]; // 右車軸の位置[rad]
    double wheel_left_joint_pos  = jointstate->position[1]; // 左車軸の位置[rad]

    // 車軸の位置は積算される
    ROS_INFO("Whell Pos (r:%f, l:%f)", wheel_r_vel,wheel_l_vel);
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "my_odom3");
    ros::NodeHandle nh;

    //subscriberの作成。トピック/cmd_velを購読する。
    //ros::Subscriber sub  = nh.subscribe("/cmd_vel", 10, cbVel);
    //ros::Subscriber sub2 = nh.subscribe("/odom", 10, cbOdom);
    //ros::Subscriber sub3 = nh.subscribe("/gazebo/model_states", 10, cbModelStates);
    ros::Subscriber sub4 = nh.subscribe("/joint_states", 100, cbMyOdom);
                
                  
    // コールバック関数を繰り返し呼び出す。
    ros::Rate rate(100);

    while (ros::ok()) {
        ros::spinOnce();
        rate.sleep();
    }
    return 0;
}
