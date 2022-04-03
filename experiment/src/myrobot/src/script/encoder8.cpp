#include <ros/ros.h>  // rosで必要はヘッダーファイル
#include <time.h>
#include <geometry_msgs/Twist.h> // ロボットを動かすために必要
#include <nav_msgs/Odometry.h>
#include <tf/transform_broadcaster.h>
#include <tf/transform_datatypes.h>
#include <gazebo_msgs/ModelStates.h> 
#include <sensor_msgs/JointState.h>
#include <std_msgs/Float64.h>
#include <std_msgs/Float64MultiArray.h>
#include <myrobot/SetVelocity2.h>

//service送信側のプログラムを書いてしまった
//clientは8

using namespace std;


struct d_pos{
  double th;
  double dt;
  double dth;
  double dx;
  double dy;
  time_t start_t;
  time_t start_r;
};

struct d_pos d_pos = {-3.14, 0, 0, 0, 0, 0, 0.01} ;

bool add (myrobot::SetVelocity2::Request &req, myrobot::SetVelocity2::Response &res){
    cout << "Linear :" << req.linear_velocity << endl;
    cout << "Angular:" << req.angular_velocity << endl; 
    //time_t start_t;
    //time_t start_r;
    time_t now;
    time_t finish;
    double t_s = req.linear_velocity;
    double r_s = req.angular_velocity;
    double ltime = 0;
    double rtime;
    double ftime;
    double pi = 3.14;
    std_msgs::Float64MultiArray msgs;
    msgs.data.resize(3);
    if (t_s != 0){
      if (d_pos.start_r != 0){
        time(&d_pos.start_t);
        time(&finish);
        ltime = finish - d_pos.start_r;
        d_pos.dth = r_s * ltime;
        d_pos.th = d_pos.th + d_pos.dth;
        d_pos.start_r = 0;
        cout << "th :" << d_pos.th << endl;
      }
      time(&now);
      ftime = now - d_pos.start_t;
      cout << "forword_time :" << ftime << endl;
    }
    if (r_s != 0){
      if (d_pos.start_t != 0){
        time(&d_pos.start_r);
        time(&finish);
        ltime = finish - d_pos.start_t;
        d_pos.dt = t_s * ltime;
        d_pos.dx = d_pos.dt * sin(d_pos.th/pi);
        d_pos.dy = d_pos.dt * cos(d_pos.th/pi);
        d_pos.start_t = 0;
        cout << "dx :" << d_pos.dx << endl;
        cout << "dy :" << d_pos.dy << endl;
      }
      time(&now);
      rtime = now - d_pos.start_r;
      cout << "rotate_time :" << rtime << endl;
    }

    msgs.data[0] = d_pos.dx;
    msgs.data[1] = d_pos.dy;
    msgs.data[2] = d_pos.dth;  
    
    ros::NodeHandle pos;
    ros::Publisher dpos = pos.advertise<std_msgs::Float64MultiArray>("msgs", 10);
    dpos.publish(msgs);
    cout << "msgs :" << msgs.data[0] << endl;
  }

// コールバック関数。並進、回転速度の表示。
void cbVel(const geometry_msgs::Twist::ConstPtr& vel) {
    cout << "Linear :" << vel->linear.x << endl;
    cout << "Angular:" << vel->angular.z << endl; 
    //time_t start_t;
    //time_t start_r;
    time_t now;
    time_t finish;
    double t_s = vel -> linear.x;
    double r_s = vel -> angular.z;
    double ltime = 0;
    double rtime;
    double ftime;
    double pi = 3.14;
    std_msgs::Float64MultiArray msgs;
    msgs.data.resize(3);
    if (t_s != 0){
      if (d_pos.start_r != 0){
        time(&d_pos.start_t);
        time(&finish);
        ltime = finish - d_pos.start_r;
        d_pos.dth = r_s * ltime;
        d_pos.th = d_pos.th + d_pos.dth;
        d_pos.start_r = 0;
        cout << "th :" << d_pos.th << endl;
      }
      time(&now);
      ftime = now - d_pos.start_t;
      cout << "forword_time :" << ftime << endl;
    }
    if (r_s != 0){
      if (d_pos.start_t != 0){
        time(&d_pos.start_r);
        time(&finish);
        ltime = finish - d_pos.start_t;
        d_pos.dt = t_s * ltime;
        d_pos.dx = d_pos.dt * sin(d_pos.th/pi);
        d_pos.dy = d_pos.dt * cos(d_pos.th/pi);
        d_pos.start_t = 0;
        cout << "dx :" << d_pos.dx << endl;
        cout << "dy :" << d_pos.dy << endl;
      }
      time(&now);
      rtime = now - d_pos.start_r;
      cout << "rotate_time :" << rtime << endl;
    }

    msgs.data[0] = d_pos.dx;
    msgs.data[1] = d_pos.dy;
    msgs.data[2] = d_pos.dth;  
    
    ros::NodeHandle pos;
    ros::Publisher dpos = pos.advertise<std_msgs::Float64MultiArray>("msgs", 10);
    dpos.publish(msgs);
    cout << "msgs :" << msgs.data[0] << endl;
   // sleep(5);
}

// /odomトピックから位置posと姿勢poseを表示 
void cbOdom(const nav_msgs::Odometry::ConstPtr& msg) { 
    ROS_INFO("Seq: %d", msg->header.seq);
    ROS_INFO("/odom Pos (x:%f, y:%f, z:%f)", msg->pose.pose.position.x,msg->pose.pose.position.y, msg->pose.pose.position.z);

    tf::Quaternion q(msg->pose.pose.orientation.x, msg->pose.pose.orientation.y, msg->pose.pose.orientation.z, msg->pose.pose.orientation.w);  
    // tf::Quaternion q(quat.x, quat.y, quat.z, quat.w);
    tf::Matrix3x3 m(q);
    double roll, pitch, yaw;
    m.getRPY(roll, pitch, yaw);

    ROS_INFO("/odom Pose (roll:%f, pitch:%f, yaw:%f) ", roll, pitch, yaw);
    ROS_INFO("Vel (Linear:%f, Angular:%f)", msg->twist.twist.linear.x,msg->twist.twist.angular.z);
                                          
}

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

// cbMyOdom：この関数に自分のオドメトリを実装しよう！
// /joint_statesトピックから左右のjoint(車輪回転軸)の位置（回転角度)[rad]を表示
// 参考：Turtlebot3の車輪直径0.066 [m]
void cbMyOdom(const sensor_msgs::JointState::ConstPtr& jointstate)
{

    //double r_vel = jointstate->velocity[0]; // 右車軸の位置[rad]
    //double l_vel  = jointstate->velocity[1]; // 左車軸の位置[rad]

    double wheel_right_joint_pos = jointstate->position[0]; // 右車軸の位置[rad]
    double wheel_left_joint_pos  = jointstate->position[1]; // 左車軸の位置[rad]

    // 車軸の位置は積算される
    ROS_INFO("Whell Pos (r:%f, l:%f)", wheel_right_joint_pos,wheel_left_joint_pos);
}

void setMyOdom()
{
  d_pos.dx = 0;
  d_pos.dy = 0;
  d_pos.dth = 0;
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "SetVelocity2");
    ros::NodeHandle nh;

    //ros::ServiceClient client = nh.serviceClient<myrobot::SetVelocity2>("SetVelocity");
    //myrobot::SetVelocity2 srv;
    //srv.request.linear_velocity = atoll(argv[1]);
   // srv.request.angular_velocity = atoll(argv[2]);
   // if (client.call(srv)){
     // cout << "linear.x :" << (double)srv.response.linear_velocity << endl;
      //cout << "angular.z :" << (double)srv.response.angular_velocity << endl;
      //ROS_INFO("linear.x: ", (double)srv.response.linear_velocity);
      //ROS_INFO("angular.z: ", (double)srv.response.angular_velocity);
    //}
    //else{
      //ROS_INFO("Failed to call service"
      //cout << "Failed to call service"  << endl;
    //}

    //subscriberの作成。トピック/cmd_velを購読する。
   // ros::Subscriber sub  = nh.subscribe("/cmd_vel", 10, cbVel);
   // ros::Subscriber sub2 = nh.subscribe("/odom", 10, cbOdom);
    //ros::Subscriber sub3 = nh.subscribe("/gazebo/model_states", 10, cbModelStates);
   // ros::Subscriber sub4 = nh.subscribe("/joint_states", 100, cbMyOdom);
    //ros::Subscriber sub5 = nh.subscribe("/joint_states", 100, setMyOdom);
    while (ros::ok()) {
      ros::ServiceServer service = nh.advertiseService("SetVelocity2", add);
    }
                   
                  
    // コールバック関数を繰り返し呼び出す。
    ros::Rate rate(100);

    while (ros::ok()) {
        ros::spinOnce();
        rate.sleep();
    }
    return 0;
}
