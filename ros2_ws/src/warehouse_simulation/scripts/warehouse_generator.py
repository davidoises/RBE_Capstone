# this script will add objects to gazebo simulation and amnge objects such ass updating positions.
import rclpy
from rclpy.node import Node
from gazebo_msgs.srv import SpawnEntity, DeleteEntity
from std_msgs.msg import Float32
import random

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

    def create_model_sdf(self, model_name, model_uri, x, y, z):
        return f"""
        <sdf version='1.6'>
            <model name='{model_name}'>
                <pose>{x} {y} {z} 0 0 0</pose>
                <include>
                    <uri>{model_uri}</uri>
                </include>
            </model>
        </sdf>
        """

    def spawn_model(self, model_name, model_xml, x, y, z):
        request = SpawnEntity.Request()
        request.name = model_name
        request.xml = model_xml
        request.robot_namespace = ''
        request.initial_pose.position.x = x
        request.initial_pose.position.y = y
        request.initial_pose.position.z = z
        self.spawn_client.call_async(request)

    def delete_model(self, model_name):
        request = DeleteEntity.Request()
        request.name = model_name
        self.delete_client.call_async(request)

    def update_temperature(self, temperature):
        msg = Float32()
        msg.data = temperature
        self.temp_publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    warehouse_generator = WarehouseGenerator()

    # Example: Spawn a person
    url = 'model://fire_truck'  # Ensure this URI is correct and the model is available
    model_xml = warehouse_generator.create_model_sdf('shelf', url, 0.0, 0.0, 0.0)
    warehouse_generator.spawn_model('shelf', model_xml, 0.0, 0.0, 0.0)

    # Example: Update temperature
    warehouse_generator.update_temperature(100.0)

    rclpy.spin(warehouse_generator)
    warehouse_generator.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()