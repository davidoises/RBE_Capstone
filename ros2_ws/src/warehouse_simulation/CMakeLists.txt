cmake_minimum_required(VERSION 3.5)
project(warehouse_simulation)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(gazebo_ros REQUIRED)

# Install Python scripts
install(PROGRAMS
  scripts/warehouse_generator.py
  DESTINATION lib/${PROJECT_NAME}
)

# Install models
install(
  DIRECTORY models/
  DESTINATION share/${PROJECT_NAME}/models
)

# Install launch files
install(
  DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/launch
)

install(
  DIRECTORY worlds/
  DESTINATION share/${PROJECT_NAME}/worlds
)

ament_package()