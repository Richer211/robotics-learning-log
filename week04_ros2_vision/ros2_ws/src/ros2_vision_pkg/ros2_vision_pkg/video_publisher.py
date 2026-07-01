import time

import cv2
import rclpy
from cv_bridge import CvBridge
from rclpy.node import Node
from sensor_msgs.msg import Image


class VideoPublisher(Node):
  """Reads a video file and publishes frames as sensor_msgs/Image."""

  def __init__(self):
    super().__init__('video_publisher')
    self.declare_parameter('video_path', '')
    self.declare_parameter('publish_rate_hz', 10.0)

    video_path = self.get_parameter('video_path').get_parameter_value().string_value
    rate_hz = self.get_parameter('publish_rate_hz').get_parameter_value().double_value

    if not video_path:
      raise RuntimeError('Set parameter video_path to a valid video file')

    self.cap = cv2.VideoCapture(video_path)
    if not self.cap.isOpened():
      raise RuntimeError(f'Cannot open video: {video_path}')

    self.publisher_ = self.create_publisher(Image, '/camera/image_raw', 10)
    self.bridge = CvBridge()
    self.timer = self.create_timer(1.0 / rate_hz, self.publish_frame)
    self.frame_id = 0
    self.get_logger().info(f'Publishing {video_path} on /camera/image_raw at {rate_hz} Hz')

  def publish_frame(self):
    ok, frame = self.cap.read()
    if not ok:
      self.get_logger().info('End of video — stopping publisher')
      self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
      return

    msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
    msg.header.stamp = self.get_clock().now().to_msg()
    msg.header.frame_id = 'camera_link'
    self.publisher_.publish(msg)
    self.frame_id += 1

  def destroy_node(self):
    self.cap.release()
    super().destroy_node()


def main(args=None):
  rclpy.init(args=args)
  node = VideoPublisher()
  try:
    rclpy.spin(node)
  except KeyboardInterrupt:
    pass
  finally:
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
  main()
