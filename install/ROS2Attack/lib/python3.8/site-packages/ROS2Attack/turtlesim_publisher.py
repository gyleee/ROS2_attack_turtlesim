import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import random
from rclpy.qos import QoSProfile, LivelinessPolicy


class TurtlebotNode(Node):
    def __init__(self):
        super().__init__('turtlesim_publisher')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(1.0, self.publish_command)


    def publish_command(self):
        linear_x = random.uniform(-2.0, 2.0)
        angular_z = random.uniform(-2.0, 2.0)
        
        
        msg = Twist()
        msg.linear.x = linear_x
        msg.angular.z = angular_z
        
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing to {self.publisher_.topic_name}: {msg}')


def main(args=None):
    rclpy.init(args=args)
    node = TurtlebotNode()
    
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()