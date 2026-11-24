cmake_minimum_required(VERSION 3.0.2)
project(jetauto_project3_ros1)

find_package(catkin REQUIRED COMPONENTS
  rospy
  geometry_msgs
)

catkin_package()

catkin_install_python(PROGRAMS
  scripts/jetauto_control_ros1.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
