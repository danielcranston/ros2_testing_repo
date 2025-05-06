#include <chrono>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/pose.hpp"

using namespace std::chrono_literals;

class Talker : public rclcpp::Node
{
public:
  Talker()
      : Node("talker"), count_(0)
  {
    publisher_ = this->create_publisher<geometry_msgs::msg::Pose>("pose", 10);
    auto timer_callback =
        [this]() -> void
    {
      auto message = geometry_msgs::msg::Pose();
      message.position.x = 1.0;
      message.orientation.x = 1.0;
      message.orientation.w = 1.0;
      RCLCPP_INFO_STREAM(this->get_logger(), "Publishing"); // << message);
      this->publisher_->publish(message);
    };
    timer_ = this->create_wall_timer(500ms, timer_callback);
  }

private:
  rclcpp::TimerBase::SharedPtr timer_;
  rclcpp::Publisher<geometry_msgs::msg::Pose>::SharedPtr publisher_;
  size_t count_;
};

int main(int argc, char *argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<Talker>());
  rclcpp::shutdown();
  return 0;
}
