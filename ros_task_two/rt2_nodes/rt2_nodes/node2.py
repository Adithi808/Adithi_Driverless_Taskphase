import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String
from rt2.msg import RT2String


class PalindromeChecker(Node):
    def __init__(self):
        super().__init__('node2_checker')
        self.last = ''
        self.create_subscription(RT2String, 'rt2_string', self.on_string, 10)
        self.flag_pub = self.create_publisher(Int32, 'palindrome_flag', 10)
        self.create_subscription(String, 'palindrome_reply', self.on_reply, 10)

    def on_string(self, msg):
        self.last = msg.data
        out = Int32()
        out.data = 1 if msg.data == msg.data[::-1] else 0
        self.flag_pub.publish(out)
        self.get_logger().info(f'Node 2 received "{msg.data}" -> sent {out.data} to Node 3')

    def on_reply(self, msg):
        self.get_logger().info(f'Node 2 got reply from Node 3 for "{self.last}": {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = PalindromeChecker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
