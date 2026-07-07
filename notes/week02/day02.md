# Week 2 Day 02 - ROS2 Node / Topic Basics

> 状态：**未开始**

## Today's Goal

- [ ] 分开运行 `distance_publisher` 和 `distance_subscriber`
- [ ] 理解 node、topic、publisher、subscriber 的关系
- [ ] 使用 `ros2 topic list`、`ros2 topic echo`、`ros2 node list` 观察系统

## 1. 学（30 分钟）

阅读：

- [`../../week02_ros2_basics/README.md`](../../week02_ros2_basics/README.md) 的 Run / Inspect 部分
- `distance_publisher.py` 和 `distance_subscriber.py` 的类名和节点名

回答：

- 什么是 ROS2 node？
- 什么是 topic？
- publisher 和 subscriber 分别做什么？
- `/sensor/distance` 是什么类型的消息？

## 2. 练（30 分钟）

在 Ubuntu VM 里开两个终端。

终端 1：

```bash
cd ~/robotics-learning-log/week02_ros2_basics/ros2_ws
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 run fake_sensor_pkg distance_publisher
```

终端 2：

```bash
cd ~/robotics-learning-log/week02_ros2_basics/ros2_ws
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 run fake_sensor_pkg distance_subscriber
```

终端 3（或停止其中一个后运行）：

```bash
ros2 topic list
ros2 topic echo /sensor/distance
ros2 node list
```

## 3. 记中文笔记（10 分钟）

- publisher 输出了什么？
- subscriber 收到了什么？
- `topic echo` 看到的 `Range` message 有哪些字段？

## 4. English Summary + Key Terms（10 分钟）

| English | 中文 |
|---------|------|
| node | 节点 |
| topic | 话题 |
| publisher | 发布者 |
| subscriber | 订阅者 |
| message | 消息 |

## 60-second Speaking Draft

Today I ran a ROS2 publisher and subscriber in separate terminals.

The publisher sends fake distance readings to the `/sensor/distance` topic.

The subscriber listens to the topic and prints a warning when the distance is too small.

I used `ros2 topic list`, `ros2 topic echo`, and `ros2 node list` to inspect the running system.

## 完成标准

- [ ] publisher 能运行
- [ ] subscriber 能收到消息
- [ ] `ros2 topic echo /sensor/distance` 有输出
- [ ] 能解释 node / topic / publisher / subscriber

## Git Commit

- Commit message：
- Pushed to GitHub：Yes / No
