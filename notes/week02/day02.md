# Week 2 Day 02 - ROS2 Node / Topic Basics

> 状态：**已完成** — publisher / subscriber 能分开运行，并能用 ROS2 命令观察 node 和 topic。

## Today's Goal

- [x] 分开运行 `distance_publisher` 和 `distance_subscriber`
- [x] 理解 node、topic、publisher、subscriber 的关系
- [x] 使用 `ros2 topic list`、`ros2 topic echo`、`ros2 node list` 观察系统

## 1. 学（30 分钟）

阅读：

- `[../../week02_ros2_basics/README.md](../../week02_ros2_basics/README.md)` 的 Run / Inspect 部分
- `distance_publisher.py` 和 `distance_subscriber.py` 的类名和节点名

回答：

### 什么是 ROS2 node？

ROS2 node 是一个正在运行的 ROS2 程序，也可以理解成机器人系统里的一个功能模块。

本项目里：

```text
distance_publisher  是一个 node
distance_subscriber 是一个 node
```

它们不是直接互相调用函数，而是通过 ROS2 topic 发送和接收 message。

`package`、`executable`、`name`、`output` 这些更像是启动 node 时需要用到的描述信息，后面学 launch file 时会更常见。

### 什么是 topic？

topic 是 ROS2 里的数据频道。

可以简单理解成：

```text
publisher 把 message 发到 topic；
subscriber 从 topic 接收 message。
```

本项目里的 topic 是：

```text
/sensor/distance
```

它负责传输假的距离传感器数据。

### publisher 和 subscriber 分别做什么？

1. publisher 负责生成假的距离读数，并发布到 `/sensor/distance`。
2. subscriber 负责订阅 `/sensor/distance`，接收距离消息，并在距离小于阈值时发出 `WARNING`。

在这个 demo 里，publisher 模拟“传感器在测距离”，subscriber 模拟“另一个程序在接收传感器数据并做判断”。

### `/sensor/distance` 是什么类型的消息？

`/sensor/distance` 传输的是 `sensor_msgs/Range` 类型的 ROS2 message。

它不是 JSON 对象。`ros2 topic echo` 显示出来的格式更像 YAML 文本，是为了方便人在终端里阅读。

这个 `Range` message 里包含：

- `header`：消息头，包含时间戳和 `frame_id`
- `radiation_type`：传感器类型
- `field_of_view`：视野角度
- `min_range`：最小测距范围
- `max_range`：最大测距范围
- `range`：当前这一次测到的距离值



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

- ros2 topic list:

```bash
    /parameter_events
    /rosout
    /sensor/distance
```

- ros2 topic echo /sensor/distance：

```bash
header:
  stamp:
    sec: 1783532892
    nanosec: 987064914
  frame_id: fake_lidar_link
radiation_type: 0
field_of_view: 0.5
min_range: 0.10000000149011612
max_range: 5.0
range: 1.3705875873565674
---
```

- ros2 node list:

```bash
/distance_publisher
```

说明：这里当时只看到 `/distance_publisher`，可能是因为检查时只有 publisher 正在运行。如果 publisher 和 subscriber 同时运行，应该能看到：

```bash
/distance_publisher
/distance_subscriber
```



## 3. 记中文笔记（10 分钟）

- publisher 输出了什么？
publisher 会生成一个假的距离值，发布到 `/sensor/distance`，同时在终端打印当前 frame 的距离。

如果：

```python
msg.range < self.WARNING_DISTANCE_M
```

就说明距离太近，会打印 `close obstacle` warning。

这里不是“距离起点多远”，而是“传感器这一次测到的物体/障碍物距离是多少”。

- subscriber 收到了什么？
subscriber 收到的是 `/sensor/distance` 这个 topic 上的 `Range` message。

它会读取 `msg.range`，然后判断距离是否小于 `WARNING_DISTANCE_M`。

如果距离小于阈值，就打印 `WARNING`；否则打印正常距离值。

- `topic echo` 看到的 `Range` message 有哪些字段？
`topic echo` 看到的 `Range` message 字段包括：
- `header`
- `stamp`
- `frame_id`
- `radiation_type`
- `field_of_view`
- `min_range`
- `max_range`
- `range`



## 4. English Summary + Key Terms（10 分钟）



## English Summary

Today I ran the ROS2 distance publisher and subscriber in separate terminals.

The publisher sends fake distance readings to the `/sensor/distance` topic.

The subscriber listens to the same topic and prints the received distance values.

I also used `ros2 topic list`, `ros2 topic echo`, and `ros2 node list` to inspect the running ROS2 system.

I learned that a topic is a communication channel, and a message is the data sent through that channel.


| English       | 中文            |
| ------------- | ------------- |
| node          | 节点            |
| topic         | 话题            |
| publisher     | 发布者           |
| subscriber    | 订阅者           |
| message       | 消息            |
| Range message | 距离范围消息        |
| frame_id      | 坐标系/传感器框架 ID  |
| topic echo    | 输出 topic 消息内容 |




## 60-second Speaking Draft

Today I ran a ROS2 publisher and subscriber in separate terminals.

The publisher sends fake distance readings to the `/sensor/distance` topic.

The subscriber listens to the topic and prints a warning when the distance is too small.

I used `ros2 topic list`, `ros2 topic echo`, and `ros2 node list` to inspect the running system.

## 完成标准

- [x] publisher 能运行
- [x] subscriber 能收到消息
- [x] `ros2 topic echo /sensor/distance` 有输出
- [x] 能解释 node / topic / publisher / subscriber



## Git Commit

- Commit message：learn day02
- Pushed to GitHub：Yes

