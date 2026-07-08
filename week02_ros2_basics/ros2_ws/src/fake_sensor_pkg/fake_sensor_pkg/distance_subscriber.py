import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range


class DistanceSubscriber(Node):
  """Subscribes to /sensor/distance and logs warnings."""

  WARNING_DISTANCE_M = 0.8

  def __init__(self):
    super().__init__('distance_subscriber')
    self.subscription = self.create_subscription(
      Range,
      '/sensor/distance',
      self.callback,
      10,
    )
    self.received = 0
    self.get_logger().info('Distance subscriber listening on /sensor/distance')

  def callback(self, msg: Range):
    self.received += 1
    if msg.range < self.WARNING_DISTANCE_M:
      self.get_logger().warn(
        f'[{self.received}] WARNING: {msg.range:.2f} m (frame_id={msg.header.frame_id})'
      )
    else:
      self.get_logger().info(f'[{self.received}] distance={msg.range:.2f} m')


def main(args=None):
  rclpy.init(args=args)
  node = DistanceSubscriber()
  try:
    rclpy.spin(node)
  except KeyboardInterrupt:
    pass
  finally:
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
  main()
