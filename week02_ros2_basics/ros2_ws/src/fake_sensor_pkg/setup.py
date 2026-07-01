from setuptools import find_packages, setup

package_name = 'fake_sensor_pkg'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/sensor_demo.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Robotics Learner',
    maintainer_email='learner@example.com',
    description='Week 2 ROS2 fake distance sensor pub/sub demo',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'distance_publisher = fake_sensor_pkg.distance_publisher:main',
            'distance_subscriber = fake_sensor_pkg.distance_subscriber:main',
        ],
    },
)
