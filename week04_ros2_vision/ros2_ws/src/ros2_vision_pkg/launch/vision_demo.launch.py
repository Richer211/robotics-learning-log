from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
  video_path = LaunchConfiguration('video_path')
  model = LaunchConfiguration('model')

  return LaunchDescription([
    DeclareLaunchArgument(
      'video_path',
      default_value='',
      description='Absolute path to input video file',
    ),
    DeclareLaunchArgument(
      'model',
      default_value='yolov8n.pt',
      description='Ultralytics model weights',
    ),
    Node(
      package='ros2_vision_pkg',
      executable='video_publisher',
      name='video_publisher',
      parameters=[{
        'video_path': video_path,
        'publish_rate_hz': 5.0,
      }],
      output='screen',
    ),
    Node(
      package='ros2_vision_pkg',
      executable='perception_node',
      name='perception_node',
      parameters=[{
        'model': model,
        'conf': 0.4,
      }],
      output='screen',
    ),
    Node(
      package='ros2_vision_pkg',
      executable='metrics_subscriber',
      name='metrics_subscriber',
      output='screen',
    ),
  ])
