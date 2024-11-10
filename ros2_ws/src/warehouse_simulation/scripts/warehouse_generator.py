#!/usr/bin/env python

import rospy
from gazebo_msgs.srv import SpawnModel, SpawnModelRequest, DeleteModel
from std_msgs.msg import Float32
import os
from rospkg import RosPack
import random
from geometry_msgs.msg import Pose

class WarehouseGenerator:
    def __init__(self):
        rospy.init_node('warehouse_generator')
        self.spawn_client = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
        self.delete_client = rospy.ServiceProxy('/gazebo/delete_model', DeleteModel)

        rospy.wait_for_service('/gazebo/spawn_sdf_model', timeout=15.0)
        
    def add_model_to_scene(self, model_pkg, x, y, z, model_name=None):
        rospack = RosPack()
        model_path = os.path.join(
            rospack.get_path('warehouse_simulation'),
            'models', model_pkg, 'model.sdf'
        )

        with open(model_path, 'r') as model_file:
            model_xml = model_file.read()
        if model_name is None:
            model_name = model_pkg
        self.spawn_model(model_name, model_xml, x, y, z)

    def spawn_model(self, model_name, model_xml, x, y, z):
        request = SpawnModelRequest()
        request.model_name = model_name
        request.model_xml = model_xml
        request.robot_namespace = ''
        request.initial_pose = Pose()
        request.initial_pose.position.x = x
        request.initial_pose.position.y = y
        request.initial_pose.position.z = z
        self.spawn_client.call(request)

    def spawn_random_people(self, num_people, x_range, y_range, z):
        for i in range(num_people):
            x = random.uniform(*x_range)
            y = random.uniform(*y_range)
            self.add_model_to_scene('person_standing', x, y, z, model_name=f'person_{i}')
        

def main():
    warehouse_generator = WarehouseGenerator()

    # Example: Spawn a shelf
    # warehouse_generator.add_model_to_scene('aws_robomaker_warehouse_ShelfF_01',0.0, 0.0, 0.0)
    # spawn in people
    warehouse_generator.spawn_random_people(3, (-30, 30), (-20, 20), 0.0)
    rospy.spin()

if __name__ == '__main__':
    main()