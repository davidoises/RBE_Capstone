# Use the official ROS 1 Noetic base image
FROM osrf/ros:noetic-desktop-full

# Set the working directory
WORKDIR /root

# Copy the setup script into the container
COPY setup.sh /root/setup.sh

# Make the setup script executable
RUN chmod +x /root/setup.sh

# Source the ROS 1 setup script
RUN /bin/bash -c "source /opt/ros/noetic/setup.bash"

# Set the entrypoint to bash
ENTRYPOINT ["/bin/bash"]