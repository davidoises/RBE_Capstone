from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),
        # Commenting out the warehouse_generator node to prevent it from starting up
        # Node(
        #     package='warehouse_simulation',
        #     executable='warehouse_generator',
        #     name='warehouse_generator',
        #     output='screen'
        # )
    ])