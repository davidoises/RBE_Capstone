from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    world_file_arg = DeclareLaunchArgument(
        'world_file',
        default_value='simple_warehouse.world',
        description='Name of the world file to load'
    )

    world_file = LaunchConfiguration('world_file')
    world_file_path = PathJoinSubstitution([
        get_package_share_directory('warehouse_simulation'),
        'worlds',
        world_file
    ])

    return LaunchDescription([
        world_file_arg,
        ExecuteProcess(
            cmd=['gazebo', '--verbose', world_file_path, '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),
        Node(
            package='warehouse_simulation',
            executable='warehouse_generator.py',
            name='warehouse_generator',
            output='screen'
        )
    ])