import rclpy
from rclpy.node import Node
from my_robot_msgs.msg import MyMessage

class SubscriberNode(Node):
    def __init__(self):
        super().__init__('subscriber_node')
        self.sub = self.create_subscription(MyMessage, 'my_topic', self.callback, 10)

    def callback(self, msg):
        self.get_logger().info(f'Received: x={msg.x}, y={msg.y}, data="{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
# This is a demo change for PR
