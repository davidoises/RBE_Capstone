# Use the official ROS 2 Jazzy base image
FROM osrf/ros:jazzy-desktop

# Set the working directory
WORKDIR /root

# Copy the setup script into the container
COPY setup.sh /root/setup.sh

# Make the setup script executable
RUN chmod +x /root/setup.sh

# Source the ROS 2 setup script
RUN /bin/bash -c "source /opt/ros/jazzy/setup.bash"

# Set the entrypoint to bash
ENTRYPOINT ["/bin/bash"]