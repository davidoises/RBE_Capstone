import rclpy
from rclpy.node import Node
from gazebo_msgs.srv import SpawnEntity, DeleteEntity
from std_msgs.msg import Float32
import os
from ament_index_python.packages import get_package_share_directory

class WarehouseGenerator(Node):
    def __init__(self):
        super().__init__('warehouse_generator')
        self.spawn_client = self.create_client(SpawnEntity, '/spawn_entity')
        self.delete_client = self.create_client(DeleteEntity, '/delete_entity')
        self.temp_publisher = self.create_publisher(Float32, 'temperature', 10)
        while not self.spawn_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('SpawnEntity service not available, waiting...')
        while not self.delete_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('DeleteEntity service not available, waiting...')

    def update_temperature(self, temperature):
        msg = Float32()
        msg.data = temperature
        self.temp_publisher.publish(msg)

    def add_shelfD_01(self, x, y, z):

        model_path = os.path.join(
            get_package_share_directory('warehouse_simulation'),
            'models', 'aws_robomaker_warehouse_ShelfD_01', 'model.sdf'
        )
        with open(model_path, 'r') as model_file:
            model_xml = model_file.read()
        self.spawn_model('aws_robomaker_warehouse_ShelfD_01', model_xml, x, y, z)

    def spawn_model(self, model_name, model_xml, x, y, z):
        request = SpawnEntity.Request()
        request.name = model_name
        request.xml = model_xml
        request.robot_namespace = ''
        request.initial_pose.position.x = x
        request.initial_pose.position.y = y
        request.initial_pose.position.z = z
        self.spawn_client.call_async(request)

def main(args=None):
    rclpy.init(args=args)
    warehouse_generator = WarehouseGenerator()

    # Example: Spawn a shelf
    warehouse_generator.add_shelfD_01(0.0, 0.0, 0.0)

    # Example: Update temperature
    warehouse_generator.update_temperature(100.0)

    rclpy.spin(warehouse_generator)
    warehouse_generator.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()