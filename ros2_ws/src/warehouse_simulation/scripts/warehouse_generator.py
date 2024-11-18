#!/usr/bin/env python

import rospy
from ros_ign_gazebo.srv import SpawnEntity
from std_msgs.msg import Float32
import os
from rospkg import RosPack
import random
from geometry_msgs.msg import Pose
import logging

class WarehouseGenerator:
    def __init__(self):
        rospy.init_node('warehouse_generator')
        self.spawn_client = rospy.ServiceProxy('/spawn_entity', SpawnEntity)

        rospy.wait_for_service('/spawn_entity', timeout=15.0)
        logging.basicConfig(level=logging.DEBUG)
        
    def add_model_to_scene(self, model_pkg, x, y, z, model_name=None):
        rospack = RosPack()
        model_path = os.path.join(
            rospack.get_path('warehouse_simulation'),
            'models', model_pkg, 'model.sdf'
        )

        if not os.path.exists(model_path):
            logging.error(f"Model path does not exist: {model_path}")
            return

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
        request.initial_pose = Pose()
        request.initial_pose.position.x = x
        request.initial_pose.position.y = y
        request.initial_pose.position.z = z
        request.initial_pose.orientation.w = 1.0
        request.initial_pose.orientation.x = 0.0
        request.initial_pose.orientation.y = 0.0
        request.initial_pose.orientation.z = 0.0
        try:
            response = self.spawn_client.call(request)
            if response.success:
                logging.info(f"Successfully spawned model: {model_name}")
            else:
                logging.error(f"Failed to spawn model: {model_name}, {response.status_message}")
        except rospy.ServiceException as e:
            logging.error(f"Service call failed: {e}")

    def spawn_random_people(self, num_people, x_range, y_range, z):
        for i in range(num_people):
            x = random.uniform(*x_range)
            y = random.uniform(*y_range)
            self.add_model_to_scene('person_standing', x, y, z, model_name=f'person_{i}')
    
    def spawn_fire(self, x, y, z):
        self.add_model_to_scene('fog_generator', x, y, z)
        

def main():
    warehouse_generator = WarehouseGenerator()

    # Example: Spawn a shelf
    # warehouse_generator.add_model_to_scene('aws_robomaker_warehouse_ShelfF_01',0.0, 0.0, 0.0)
    # spawn in people
    # warehouse_generator.spawn_random_people(3, (-30, 30), (-20, 20), 0.0)
    # spawn fire
    warehouse_generator.spawn_fire(0.0, 0.0, 0.0)
    rospy.spin()

if __name__ == '__main__':
    main()