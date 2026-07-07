# Week 2 Day 05 - ROS2 Bag Record / Playback

> 状态：**未开始**

## Today's Goal

- [ ] 使用 `ros2 bag record` 录制 `/sensor/distance`
- [ ] 使用 `ros2 bag play` 回放数据
- [ ] 理解 rosbag 和机器人数据记录的关系

## 1. 学（30 分钟）

阅读 [`../../week02_ros2_basics/README.md`](../../week02_ros2_basics/README.md) 的 Rosbag 部分。

回答：

- rosbag 是什么？
- 为什么机器人开发需要录制传感器数据？
- `record` 和 `play` 分别做什么？
- 为什么 rosbag 对调试 perception / control 很重要？

## 2. 练（30 分钟）

终端 1：启动 publisher / subscriber：

```bash
cd ~/robotics-learning-log/week02_ros2_basics/ros2_ws
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 launch fake_sensor_pkg sensor_demo.launch.py
```

终端 2：录制 topic：

```bash
cd ~/robotics-learning-log/week02_ros2_basics/ros2_ws
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 bag record /sensor/distance -o bags/week02_distance
```

按 `Ctrl+C` 停止录制后，回放：

```bash
ros2 bag play bags/week02_distance
```

## 3. 记中文笔记（10 分钟）

- rosbag 生成了哪些文件？
- 回放时 subscriber 能否收到数据？
- 录制/回放对真实机器人调试有什么帮助？

## 4. English Summary + Key Terms（10 分钟）

| English | 中文 |
|---------|------|
| rosbag | ROS 数据包 |
| record | 录制 |
| playback | 回放 |
| telemetry | 遥测/运行数据 |
| data logging | 数据记录 |

## 60-second Speaking Draft

Today I practiced recording and playing back ROS2 topic data with rosbag.

I recorded the `/sensor/distance` topic while the fake sensor publisher was running.

Then I played the bag file back to reproduce the same sensor data.

This is useful in robotics because we can debug software without running the real robot every time.

## 完成标准

- [ ] 成功 `ros2 bag record`
- [ ] 成功 `ros2 bag play`
- [ ] 能解释 rosbag 的用途
- [ ] 本日志已填写

## Git Commit

- Commit message：
- Pushed to GitHub：Yes / No
