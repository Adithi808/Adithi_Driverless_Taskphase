import rclpy
from rclpy.node import Node
from rt2.msg import RT2String


class StringPublisher(Node):
    def __init__(self):
        super().__init__('node1_publisher')
        self.pub = self.create_publisher(RT2String, 'rt2_string', 10)


def main(args=None):
    rclpy.init(args=args)
    node = StringPublisher()
    try:
        while rclpy.ok():
            text = input('Enter a string: ').strip()
            if not text:
                print('Please enter a non-empty string.')
                continue
            msg = RT2String()
            msg.data = text
            node.pub.publish(msg)
            node.get_logger().info(f'Node 1 published: "{text}"')
    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
