import json

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MetricsSubscriber(Node):
  """Logs perception metrics and detection summaries."""

  def __init__(self):
    super().__init__('metrics_subscriber')
    self.create_subscription(String, '/perception/metrics', self.metrics_callback, 10)
    self.create_subscription(String, '/perception/detections', self.detections_callback, 10)
    self.get_logger().info('Metrics subscriber listening')

  def metrics_callback(self, msg: String):
    data = json.loads(msg.data)
    self.get_logger().info(
      f"METRICS frame={data['frame']} infer_ms={data['infer_ms']} "
      f"total_ms={data['total_ms']} avg_ms={data['avg_ms']} fps={data['fps']}"
    )

  def detections_callback(self, msg: String):
    data = json.loads(msg.data)
    if data['count'] > 0:
      labels = [d['label'] for d in data['detections']]
      self.get_logger().info(f"DETECTIONS count={data['count']} labels={labels}")


def main(args=None):
  rclpy.init(args=args)
  node = MetricsSubscriber()
  try:
    rclpy.spin(node)
  except KeyboardInterrupt:
    pass
  finally:
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
  main()
