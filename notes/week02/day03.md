# Week 2 Day 03 - Read ROS2 Publisher / Subscriber Code

> 状态：**未开始**

## Today's Goal

- [ ] 读懂 `distance_publisher.py`
- [ ] 读懂 `distance_subscriber.py`
- [ ] 理解 `rclpy`、`Node`、`Range`、timer、callback

## 1. 学（30 分钟）

重点阅读：

- `week02_ros2_basics/ros2_ws/src/fake_sensor_pkg/fake_sensor_pkg/distance_publisher.py`
- `week02_ros2_basics/ros2_ws/src/fake_sensor_pkg/fake_sensor_pkg/distance_subscriber.py`

回答：

- `DistancePublisher(Node)` 为什么继承 `Node`？
- `create_publisher(Range, '/sensor/distance', 10)` 三个参数分别是什么？
- `create_timer(0.5, self.publish_reading)` 表示什么？
- subscriber 的 `callback(self, msg)` 什么时候被调用？
- `rclpy.spin(node)` 为什么不能省略？

## 2. 练（30 分钟）

在 VM 中重新运行 Day 02 demo，并边运行边看代码：

```bash
cd ~/robotics-learning-log/week02_ros2_basics/ros2_ws
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 launch fake_sensor_pkg sensor_demo.launch.py
```

观察输出后按 `Ctrl+C` 停止。

可选：把 subscriber 的 warning 阈值从 `1.0` 改成 `0.8`，重新 build/run，对比 WARNING 次数。

## 3. 记中文笔记（10 分钟）

- publisher 的主流程
- subscriber 的主流程
- `Range` message 里你认识的字段
- 目前最不懂的一行代码

## 4. English Summary + Key Terms（10 分钟）

| English | 中文 |
|---------|------|
| rclpy | ROS2 Python 客户端库 |
| callback | 回调函数 |
| timer | 定时器 |
| Range message | 距离范围消息 |
| spin | 让节点持续处理事件 |

## 60-second Speaking Draft

Today I read the ROS2 publisher and subscriber code.

The publisher creates a `Range` message and publishes it every 0.5 seconds.

The subscriber receives the message in a callback function.

I learned that `rclpy.spin()` keeps a ROS2 node alive so it can process timers and messages.

## 完成标准

- [ ] 能解释 publisher 代码主流程
- [ ] 能解释 subscriber 代码主流程
- [ ] 能说出 `callback` 什么时候触发
- [ ] 本日志已填写

## Git Commit

- Commit message：
- Pushed to GitHub：Yes / No
