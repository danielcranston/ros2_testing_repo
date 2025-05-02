#include <gtest/gtest.h>

#include <geometry_msgs/msg/pose.hpp>

TEST(kilted_tutorial_party_340, test_linking_with_geometry_msgs) {
  geometry_msgs::msg::Pose pose;
  ASSERT_EQ(pose.orientation.w, 1.0);
}

int main(int argc, char **argv) {
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
