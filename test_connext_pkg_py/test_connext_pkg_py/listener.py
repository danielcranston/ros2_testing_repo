import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node

from geometry_msgs.msg import Pose


class PoseListenerNode(Node):

    def __init__(self):
        super().__init__("pose_listener_node")
        self.subscription = self.create_subscription(Pose, "pose", self.listener_callback, 10)

    def listener_callback(self, msg):
        self.get_logger().info(f"I heard: {msg}")


def main(args=None):
    try:
        with rclpy.init(args=args):
            pose_listener_node = PoseListenerNode()

            rclpy.spin(pose_listener_node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == "__main__":
    main()
