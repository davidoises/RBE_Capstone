#!/bin/bash

# Update and install necessary packages
sudo apt update -y

sudo apt install nano -y
sudo apt install git -y
sudo apt install python3-pip -y
sudo apt install python3-colcon-common-extensions -y
sudo apt install -y python3-rosinstall-generator
sudo apt install -y python3-vcstool
sudo apt-get -y install python3-catkin-tools


#https://docs.clearpathrobotics.com/docs/ros1noetic/robots/outdoor_robots/jackal/tutorials_jackal/
sudo apt-get install -y ros-noetic-jackal-simulator ros-noetic-jackal-desktop ros-noetic-jackal-navigation
pip3 install ultralytics

sudo apt-get update
sudo apt-get install lsb-release wget gnupg -y

sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
sudo apt-get update -y

sudo apt-get install -y ignition-edifice
sudo apt-get install -y ros-noetic-ros-ign-gazebo

# # Source the ROS 2 setup script
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
echo "export IGNITION_VERSION=edifice" >> ~/.bashrc
echo "export IGN_GAZEBO_RESOURCE_PATH=$IGN_GAZEBO_RESOURCE_PATH:~/UrbanFireRobot/ros2_ws/install/share/warehouse_simulation/models" >> ~/.bashrc
source ~/.bashrc

# Create a workspace
# cd ~/ros2_ws
# colcon build
# source ~/ros2_ws/install/setup.bash

# colcon
# export IGN_GAZEBO_RESOURCE_PATH=$IGN_GAZEBO_RESOURCE_PATH:~/ros2_ws/install/warehouse_simulation/share/warehouse_simulation/models
# catkin
# export IGN_GAZEBO_RESOURCE_PATH=$IGN_GAZEBO_RESOURCE_PATH:~/ros2_ws/src/warehouse_simulation/models

# export JACKAL_URDF_EXTRAS=~/ros2_ws/src/warehouse_simulation/description/camera.xacro