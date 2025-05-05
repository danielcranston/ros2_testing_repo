import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
import rclpy.parameter

from rclpy.parameter_event_handler import ParameterEventHandler
from rcl_interfaces.msg import ParameterEvent


class SampleNodeWithParameters(Node):
    def __init__(self):
        super().__init__("node_with_parameters")

        self.declare_parameter("an_int_param", 0)
        self.declare_parameter("another_double_param", 0.0)

        self.handler = ParameterEventHandler(self)

        self.callback_handle = self.handler.add_parameter_callback(
            parameter_name="an_int_param",
            node_name="node_with_parameters",
            callback=self.callback,
        )
        self.callback_handle2 = self.handler.add_parameter_callback(
            parameter_name="a_double_param",
            node_name="parameter_blackboard",
            callback=self.callback,
        )

        self.callback_handle3 = self.handler.add_parameter_event_callback(
            callback=self.event_callback,
        )

    def callback(self, p: rclpy.parameter.Parameter) -> None:
        self.get_logger().info(
            f"Received an update to parameter: {p.name}: {rclpy.parameter.parameter_value_to_python(p.value)}"
        )

    def event_callback(self, event: ParameterEvent):
        """
        ros2 service call /node_with_parameters/set_parameters_atomically rcl_interfaces/srv/SetParametersAtomically "parameters: [{name: an_int_param, value: {type: 2, integer_value: 1}}, {name: an_int_param, value: {type: 2, integer_value: 1}}]"
        """
        self.get_logger().info("Received parameter event")

        for p in event.changed_parameters:
            self.get_logger().info(
                f"Inside event: {p.name} changed to: {rclpy.parameter.parameter_value_to_python(p.value)}"
            )


def main():
    try:
        with rclpy.init():
            node = SampleNodeWithParameters()
            rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
