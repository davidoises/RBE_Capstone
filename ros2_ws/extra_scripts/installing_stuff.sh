#!/bin/bash

# Dependencies

# ROS
sudo apt-get install -y ros-noetic-navigation
sudo apt-get install -y ros-noetic-robot-localization
sudo apt-get install -y ros-noetic-robot-state-publisher

# Add add-apt-repository command
sudo apt-get -y install software-properties-common
sudo apt-get update

# GTSAM
sudo add-apt-repository ppa:borglab/gtsam-release-4.0
sudo apt update

sudo apt install -y libgtsam-dev libgtsam-unstable-dev

# Add git
sudo apt install -y git