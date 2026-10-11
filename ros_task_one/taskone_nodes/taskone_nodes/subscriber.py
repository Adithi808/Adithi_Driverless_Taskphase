import rclpy
from rclpy.node import Node
from taskone.msg import TaskOne


class WheelSubscriber(Node):
    def __init__(self):
        super().__init__('wheel_subscriber')
        self.sub = self.create_subscription(TaskOne, '/taskone', self.callback, 10)

    def callback(self, msg):
        speed = msg.angvel * msg.radius  # v = ω × r
        self.get_logger().info(
            f'angvel={msg.angvel:.2f} rad/s, radius={msg.radius:.2f} m '
            f'-> longitudinal speed = {speed:.2f} m/s')


def main(args=None):
    rclpy.init(args=args)
    node = WheelSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()