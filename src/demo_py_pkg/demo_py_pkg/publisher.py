import rclpy
from rclpy.node import Node
from my_robot_msgs.msg import MyMessage

class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher_node')
        self.pub = self.create_publisher(MyMessage, 'my_topic', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.counter = 0

    def timer_callback(self):
        msg = MyMessage()
        msg.x = float(self.counter)
        msg.y = float(self.counter * 2)
        msg.data = f"Hello {self.counter}"
        self.pub.publish(msg)
        self.get_logger().info(f'Published: x={msg.x}, y={msg.y}, data="{msg.data}"')
        self.counter += 1

def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
