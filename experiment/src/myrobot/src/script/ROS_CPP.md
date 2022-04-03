# Rosで.cppから.exeファイルを作成する

*CMakeListsの一番下へ以下を追加 

'cmake_minimum_required(VERSION 2.8)'
'add_executable(encoder src/script/encoder.cpp)'
'target_link_libraries(encoder ${catkin_LIBRARIES})'

* 2行目 encoder は実行する時に使う名前, encoder.cppは実行フィルを作成するcppファイル名
* 3行目 encoder は2行目に決めた実行するときに使う名前となる

* 最後にcatkin_makeをして成功すれば実行できる  

# 実行方法
'rosrun myrobot encoder'

* myrobotはパッケージ名である
* encoderは実行するときに使う名前
* roscoreを起動してから行うようにする

***  
参考サイト  
* <https://qiita.com/termoshtt/items/539541c180dfc40a1189>  
* <http://forestofazumino.web.fc2.com/ros/ros_simple_program.html>
