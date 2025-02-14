import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class TurtlebotSubNode(Node):
    def __init__(self):
        super().__init__('turtlesim_subscriber')

        self.subscription = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)

    
    def pose_callback(self, msg):
        self.get_logger().info(f'Received Pose: x={msg.x}, y={msg.y}, theta={msg.theta}')



def main(args=None):
    rclpy.init(args=args)
    node = TurtlebotSubNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()