#!/bin/bash

# Update and install necessary packages
sudo apt update -y

sudo apt install nano -y
sudo apt install python3-pip -y
sudo apt install python3-colcon-common-extensions -y
sudo apt install -y python3-rosinstall-generator
sudo apt install -y python3-vcstool

sudo apt-get install -y ignition-edifice
sudo apt-get install -y ros-noetic-ros-ign-gazebo

# sudo apt-get install -y ros-noetic-ros-ign-gazebo
# sudo apt install -y ros-noetic-ros-ign-bridge
# sudo apt-get install ignition-citadel -y

#https://docs.clearpathrobotics.com/docs/ros1noetic/robots/outdoor_robots/jackal/tutorials_jackal/
sudo apt-get install -y ros-noetic-jackal-simulator ros-noetic-jackal-desktop ros-noetic-jackal-navigation
pip3 install ultralytics

# # Source the ROS 2 setup script
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc

# Create a workspace
# cd ~/ros2_ws
# colcon build
# source ~/ros2_ws/install/setup.bash

# export IGN_GAZEBO_RESOURCE_PATH=$IGN_GAZEBO_RESOURCE_PATH:~/ros2_ws/install/warehouse_simulation/share/warehouse_simulation/models

# export JACKAL_URDF_EXTRAS=~/ros2_ws/src/warehouse_simulation/description/camera.xacro