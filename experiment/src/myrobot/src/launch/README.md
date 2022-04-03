mysensor_v5.launch




mysensor_v6.launch
tfへ情報をsubscribeすることでロボットを移動できるようにする
参考サイト: https://qiita.com/srs/items/5848c6b05e5f8a0827f9
起動するときにpositionを加える必要がある
roslaunch myrobot mysensor_v6.launch position:=gazebo



ロボットの位置情報を知りたい時
rostopic echo /gazebo/model_states
