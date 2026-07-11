import random

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range


class DistancePublisher(Node):
  """Publishes simulated distance readings on /sensor/distance."""

  WARNING_DISTANCE_M = 1.0

  def __init__(self):
    super().__init__('distance_publisher')
    self.publisher_ = self.create_publisher(Range, '/sensor/distance', 10)
    self.timer = self.create_timer(0.5, self.publish_reading)
    self.frame = 0
    self.get_logger().info('Distance publisher started on /sensor/distance')

  def publish_reading(self):
    msg = Range()
    msg.header.stamp = self.get_clock().now().to_msg()
    msg.header.frame_id = 'fake_lidar_link'
    msg.radiation_type = Range.ULTRASOUND
    msg.field_of_view = 0.5
    msg.min_range = 0.1
    msg.max_range = 5.0
    msg.range = random.uniform(msg.min_range, msg.max_range)

    self.publisher_.publish(msg)

    if msg.range < self.WARNING_DISTANCE_M:
      self.get_logger().warn(f'Frame {self.frame}: close obstacle at {msg.range:.2f} m')
    else:
      self.get_logger().info(f'Frame {self.frame}: distance={msg.range:.2f} m')

    self.frame += 1


def main(args=None):
  rclpy.init(args=args)
  node = DistancePublisher()
  try:
    rclpy.spin(node)
  except KeyboardInterrupt:
    pass
  finally:
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
  main()
