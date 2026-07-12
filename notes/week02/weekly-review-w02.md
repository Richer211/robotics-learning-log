# Weekly Review - Week 2

> 主题：ROS2 Basics

## 1. What I Built

- [x] ROS2 workspace built successfully
- [x] Fake distance sensor publisher
- [x] Distance subscriber
- [x] Launch file
- [x] Rosbag record / playback workflow

## 2. What I Learned（中文）

### ROS2 基础概念

写下你对以下概念的理解：

- node：正在运行的 ROS2 程序或功能模块，例如 `distance_publisher` 和 `distance_subscriber`。
- topic：ROS2 里的数据频道，例如 `/sensor/distance`。
- publisher：某个 node 里的发布者，负责把 message 发到 topic。
- subscriber：某个 node 里的订阅者，负责从 topic 接收 message。
- message：topic 上传输的数据结构，例如 `sensor_msgs/Range`。
- launch file：用一条命令启动和管理多个 ROS2 node 的文件。
- rosbag：录制和回放 topic message 的工具。

### 本周最重要的 3 个收获

1. 跑通了 ROS2 Humble + `colcon build` + publisher / subscriber 的完整最小流程。
2. 理解了 node、topic、message、publisher、subscriber 的通信关系。
3. 学会了用 launch file 一次启动多个 node，并用 rosbag 录制和回放 topic 数据。

## 3. Problems I Met

- 问题 1：新终端找不到 `fake_sensor_pkg`。
- 问题 2：一开始误以为 `WARNING_DISTANCE_M` 会随着 topic message 一起发送。
- 问题 3：一开始不清楚 `rosbag` 记录的是 publisher 程序还是 topic message。

## 4. How I Solved Them

- 解决方式 1：每个新终端都先执行 `source /opt/ros/humble/setup.bash` 和 `source install/setup.bash`。
- 解决方式 2：通过修改 publisher / subscriber 阈值并观察输出，确认 topic 里发送的是 `msg.range`，不是 warning threshold。
- 解决方式 3：通过 `ros2 bag record` 和 `ros2 bag play` 实操，理解 rosbag 录制的是 topic message。

## 5. English Summary

This week I learned the basics of ROS2.

I built and ran a fake distance sensor demo with a publisher and a subscriber.

I learned how ROS2 nodes communicate through topics and messages.

I also practiced using launch files and rosbag to run and debug a simple robotics system.

## 6. Key Terms

| English | 中文 | Note |
|---------|------|------|
| ROS2 | 机器人操作系统第二代 | Robotics middleware |
| node | 节点 | A running ROS2 program |
| topic | 话题 | A named communication channel |
| publisher | 发布者 | Sends messages to a topic |
| subscriber | 订阅者 | Receives messages from a topic |
| message | 消息 | Structured data sent through topics |
| launch file | 启动文件 | Starts one or more nodes |
| rosbag | ROS 数据包 | Records and replays topic data |

## 7. 60-second Speaking Draft

This week I learned the basics of ROS2.

I built a fake distance sensor system with two nodes.

One node publishes distance messages, and the other node subscribes to those messages.

I also used a launch file to start both nodes together.

Finally, I practiced recording and playing back topic data with rosbag.

These tools are important because real robots have many nodes, many topics, and a lot of sensor data.

## 8. Next Week Plan

- [x] Start Week 3 vision / perception demo
- [x] Review basic image concepts
- [x] Learn how camera data may connect to ROS2 later
- [x] Continue English Summary and Speaking Draft
