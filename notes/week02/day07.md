# Week 2 Day 07 - Review and Prepare for Week 3

> 状态：**已完成** — Week 2 ROS2 基础复盘完成，准备进入 Week 3 perception / vision。

## Today's Goal

- [x] 完成 Week 2 复盘
- [x] 整理 ROS2 基础概念
- [x] 更新 glossary
- [x] 准备 Week 3 perception / vision 学习

## 1. 回顾（30 分钟）

检查 Week 2 是否完成：

- [x] ROS2 Humble 环境可用
- [x] `colcon build --symlink-install` 成功
- [x] publisher / subscriber 可以分开运行
- [x] launch file 可以一键启动
- [x] rosbag 可以录制和回放
- [x] 至少完成一次小改动并验证

## 2. 复盘问题（30 分钟）

写在 [`weekly-review-w02.md`](weekly-review-w02.md)：

- Week 2 最重要的 3 个收获是什么？
1. 成功在 Ubuntu VM 里安装和使用 ROS2 Humble，并理解了 node、topic、message、publisher、subscriber 的关系。
2. 使用两种方式运行 publisher / subscriber：一种是 `ros2 run` 分别启动节点，另一种是 `ros2 launch` 一次启动多个节点。
3. 学会了 ROS2 workspace 的基本流程：`source /opt/ros/humble/setup.bash`、`colcon build --symlink-install`、`source install/setup.bash`、`ros2 run` / `ros2 launch`。

- ROS2 里 node / topic / publisher / subscriber 的关系是什么？

node 是正在运行的 ROS2 程序或功能模块。

publisher 是某个 node 里的发布者，负责把 message 发到 topic。

subscriber 是某个 node 里的订阅者，负责从 topic 接收 message。

topic 是数据频道，不是“负责接收 message”的对象。

message 是 topic 上传输的数据结构。

本项目里的关系是：

```text
distance_publisher node
  -> publisher
  -> /sensor/distance topic
  -> Range message
  -> subscriber
  -> distance_subscriber node
```

- `colcon build`、`source install/setup.bash`、`ros2 run`、`ros2 launch` 的流程是什么？

- `colcon build --symlink-install`：构建 ROS2 workspace 里的 package，并生成 `build/`、`install/`、`log/` 等构建结果。
- `source install/setup.bash`：让当前终端认识刚刚 build 好的 package。它不是负责生成 `install/`，生成过程是 `colcon build` 做的。
- `ros2 run`：运行某个 package 里的一个 executable，例如 `distance_publisher`。
- `ros2 launch`：根据 launch file 一次启动多个 node，例如同时启动 publisher 和 subscriber。

最小流程是：

```bash
cd ~/robotics-learning-log/week02_ros2_basics/ros2_ws
source /opt/ros/humble/setup.bash
colcon build --symlink-install
source install/setup.bash
ros2 launch fake_sensor_pkg sensor_demo.launch.py
```

- rosbag 为什么重要？

rosbag 可以录制 topic message，并按时间顺序回放。

它重要是因为真实机器人运行一次成本高，环境也不一定能完全重复。录制下来之后，可以不用反复运行真实机器人，也能用同一段传感器数据调试 perception、control、planning 等算法。

- 还有哪些概念不清楚？
ROS2 除了 node / topic / launch / rosbag 之外，我还想继续了解：

- 怎么模拟机器人运动
- 有没有实时界面显示机器人状态或移动
- RViz 和 Gazebo 分别解决什么问题
- camera / image data 后续如何进入 ROS2 perception pipeline

这些问题可以放到 Week 3 / Week 4 继续学习。

## 3. English Summary + Key Terms（10 分钟）

## English Summary

This week I learned the basics of ROS2.

I built and ran a fake distance sensor system with a publisher and a subscriber.

I learned that ROS2 nodes communicate through topics, and topics carry structured messages.

I also practiced using a launch file to start multiple nodes and rosbag to record and replay topic data.

Next week I plan to start learning basic computer vision and perception, and later connect image data back to ROS2.

整理 Week 2 Key Terms，并同步到 [`../glossary/robotics-terms.md`](../glossary/robotics-terms.md)：

| English | 中文 |
|---------|------|
| ROS2 node | ROS2 节点 |
| topic graph | 话题图 |
| launch system | 启动系统 |
| rosbag playback | rosbag 回放 |
| robotics middleware | 机器人中间件 |
| perception | 感知 |
| vision pipeline | 视觉流程 |

## 60-second Speaking Draft

This week I learned the basics of ROS2.

I built a small fake distance sensor system with a publisher and a subscriber.

The publisher sends `Range` messages to a topic, and the subscriber receives those messages.

I also learned how to start multiple nodes with a launch file and how to record topic data with rosbag.

Next week I plan to start learning basic computer vision and perception.

## 4. Git 收尾

```bash
git status
git add notes/week02 notes/glossary/robotics-terms.md
git commit -m "Add Week 2 ROS2 learning plans and review"
git push
```

## 完成标准

- [x] `weekly-review-w02.md` 已填写
- [x] glossary 已更新 Week 2 词汇
- [x] Git 已 commit / push
- [x] 明确 Week 3 下一步
