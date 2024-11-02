#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from gazebo_msgs.srv import SpawnEntity, DeleteEntity
from std_msgs.msg import Float32
import os
from ament_index_python.packages import get_package_share_directory
import random

class WarehouseGenerator(Node):
    def __init__(self):
        super().__init__('warehouse_generator')
        self.spawn_client = self.create_client(SpawnEntity, '/spawn_entity')
        self.delete_client = self.create_client(DeleteEntity, '/delete_entity')

        while not self.spawn_client.wait_for_service(timeout_sec=15.0):
            self.get_logger().info('Waiting for spawn_entity service...')
            if self.spawn_client.service_is_ready():
                break
            else:
                self.get_logger().error('spawn_entity service not available, exiting...')
                rclpy.shutdown()
                exit(1)
        
    def add_model_to_scene(self, model_pkg, x, y, z, model_name=None):
        model_path = os.path.join(
            get_package_share_directory('warehouse_simulation'),
            'models', model_pkg, 'model.sdf'
        )

        with open(model_path, 'r') as model_file:
            model_xml = model_file.read()
        if model_name is None:
            model_name = model_pkg
        self.spawn_model(model_name, model_xml, x, y, z)

    def spawn_model(self, model_name, model_xml, x, y, z):
        request = SpawnEntity.Request()
        request.name = model_name
        request.xml = model_xml
        request.robot_namespace = ''
        request.initial_pose.position.x = x
        request.initial_pose.position.y = y
        request.initial_pose.position.z = z
        self.spawn_client.call_async(request)

    def spawn_random_people(self, num_people, x_range, y_range, z):
        for i in range(num_people):
            x = random.uniform(*x_range)
            y = random.uniform(*y_range)
            self.add_model_to_scene('person_standing', x, y, z, model_name=f'person_{i}')
        

def main(args=None):
    rclpy.init(args=args)
    warehouse_generator = WarehouseGenerator()

    # Example: Spawn a shelf
    # warehouse_generator.add_model_to_scene('aws_robomaker_warehouse_ShelfF_01',0.0, 0.0, 0.0)
    # spawn in people
    warehouse_generator.spawn_random_people(3, (-30, 30), (-20, 20), 0.0)
    rclpy.spin(warehouse_generator)
    warehouse_generator.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()