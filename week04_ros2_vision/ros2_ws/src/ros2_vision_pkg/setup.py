from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'ros2_vision_pkg'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Robotics Learner',
    maintainer_email='learner@example.com',
    description='Week 4 ROS2 perception pipeline',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'video_publisher = ros2_vision_pkg.video_publisher:main',
            'perception_node = ros2_vision_pkg.perception_node:main',
            'metrics_subscriber = ros2_vision_pkg.metrics_subscriber:main',
        ],
    },
)
