from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
  return LaunchDescription([
    Node(
      package='fake_sensor_pkg',
      executable='distance_publisher',
      name='distance_publisher',
      output='screen',
    ),
    Node(
      package='fake_sensor_pkg',
      executable='distance_subscriber',
      name='distance_subscriber',
      output='screen',
    ),
  ])
