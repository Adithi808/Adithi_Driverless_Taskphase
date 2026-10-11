import time

import rclpy
from rclpy.node import Node
from taskone.msg import TaskOne


class WheelPublisher(Node):
    def __init__(self):
        super().__init__('wheel_publisher')
        self.pub = self.create_publisher(TaskOne, '/taskone', 10)


def main(args=None):
    rclpy.init(args=args)
    node = WheelPublisher()
    try:
        try:
            angvel = float(input('Enter angular velocity (rad/s): '))
            radius = float(input('Enter wheel radius (m): '))
        except ValueError:
            print('Please enter valid numbers.')
            return

        msg = TaskOne()
        msg.angvel = angvel
        msg.radius = radius

        time.sleep(1.0)  # let the subscriber connect before publishing
        node.pub.publish(msg)
        node.get_logger().info(f'Published: angvel={angvel}, radius={radius}')
        time.sleep(0.5)  # let the message go out before shutting down
    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()