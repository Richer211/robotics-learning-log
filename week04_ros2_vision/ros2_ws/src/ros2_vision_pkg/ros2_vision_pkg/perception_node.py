import json
import time

import rclpy
from cv_bridge import CvBridge
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import String


class PerceptionNode(Node):
  """Subscribes to images, runs YOLO, publishes detections and latency metrics."""

  def __init__(self):
    super().__init__('perception_node')
    self.declare_parameter('model', 'yolov8n.pt')
    self.declare_parameter('conf', 0.4)

    model_name = self.get_parameter('model').get_parameter_value().string_value
    conf = self.get_parameter('conf').get_parameter_value().double_value

    try:
      from ultralytics import YOLO
    except ImportError as exc:
      raise RuntimeError('pip install ultralytics inside ROS2 environment') from exc

    self.model = YOLO(model_name)
    self.conf = conf
    self.bridge = CvBridge()

    self.det_pub = self.create_publisher(String, '/perception/detections', 10)
    self.metrics_pub = self.create_publisher(String, '/perception/metrics', 10)
    self.create_subscription(Image, '/camera/image_raw', self.image_callback, 10)

    self.frame_count = 0
    self.total_latency_ms = 0.0
    self.get_logger().info(f'Perception node ready (model={model_name})')

  def image_callback(self, msg: Image):
    receive_time = time.perf_counter()
    frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

    start = time.perf_counter()
    results = self.model.predict(frame, conf=self.conf, verbose=False)
    infer_ms = (time.perf_counter() - start) * 1000.0
    total_ms = (time.perf_counter() - receive_time) * 1000.0

    boxes = []
    for box in results[0].boxes:
      cls_id = int(box.cls[0])
      label = results[0].names[cls_id]
      conf = float(box.conf[0])
      xyxy = [float(v) for v in box.xyxy[0].tolist()]
      boxes.append({'label': label, 'conf': conf, 'xyxy': xyxy})

    detection_msg = String()
    detection_msg.data = json.dumps({
      'stamp': msg.header.stamp.sec + msg.header.stamp.nanosec * 1e-9,
      'frame_id': msg.header.frame_id,
      'count': len(boxes),
      'detections': boxes,
    })
    self.det_pub.publish(detection_msg)

    self.frame_count += 1
    self.total_latency_ms += total_ms
    avg_ms = self.total_latency_ms / self.frame_count
    fps = 1000.0 / avg_ms if avg_ms > 0 else 0.0

    metrics_msg = String()
    metrics_msg.data = json.dumps({
      'frame': self.frame_count,
      'infer_ms': round(infer_ms, 2),
      'total_ms': round(total_ms, 2),
      'avg_ms': round(avg_ms, 2),
      'fps': round(fps, 2),
    })
    self.metrics_pub.publish(metrics_msg)

    if self.frame_count % 10 == 0:
      self.get_logger().info(
        f'Frame {self.frame_count}: {len(boxes)} detections, '
        f'infer={infer_ms:.1f}ms, avg={avg_ms:.1f}ms, fps={fps:.1f}'
      )


def main(args=None):
  rclpy.init(args=args)
  node = PerceptionNode()
  try:
    rclpy.spin(node)
  except KeyboardInterrupt:
    pass
  finally:
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
  main()
