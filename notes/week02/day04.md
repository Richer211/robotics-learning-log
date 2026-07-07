# Week 2 Day 04 - ROS2 Launch File

> 状态：**未开始**

## Today's Goal

- [ ] 理解 launch file 的作用
- [ ] 使用一条命令同时启动 publisher 和 subscriber
- [ ] 读懂 `sensor_demo.launch.py`

## 1. 学（30 分钟）

阅读：

- `week02_ros2_basics/ros2_ws/src/fake_sensor_pkg/launch/sensor_demo.launch.py`
- [`../../week02_ros2_basics/README.md`](../../week02_ros2_basics/README.md) 的 Launch 部分

回答：

- launch file 解决什么问题？
- `Node(package=..., executable=..., name=..., output='screen')` 每个字段是什么意思？
- launch 和手动开两个终端运行有什么区别？

## 2. 练（30 分钟）

在 Ubuntu VM 中执行：

```bash
cd ~/robotics-learning-log/week02_ros2_basics/ros2_ws
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 launch fake_sensor_pkg sensor_demo.launch.py
```

另开一个终端观察：

```bash
source /opt/ros/humble/setup.bash
source ~/robotics-learning-log/week02_ros2_basics/ros2_ws/install/setup.bash
ros2 node list
ros2 topic list
```

## 3. 记中文笔记（10 分钟）

- launch file 和手动运行两个节点的差异
- `output='screen'` 的作用
- 什么时候需要 launch file？

## 4. English Summary + Key Terms（10 分钟）

| English | 中文 |
|---------|------|
| launch file | 启动文件 |
| executable | 可执行入口 |
| package | ROS2 包 |
| process | 进程 |
| output | 输出 |

## 60-second Speaking Draft

Today I learned how to use a ROS2 launch file.

The launch file starts both the distance publisher and the distance subscriber with one command.

This is useful because real robot systems often need many nodes to run together.

I also used `ros2 node list` and `ros2 topic list` to verify that the nodes were running.

## 完成标准

- [ ] `ros2 launch fake_sensor_pkg sensor_demo.launch.py` 成功
- [ ] 能解释 `sensor_demo.launch.py`
- [ ] 能用 `ros2 node list` 验证两个节点
- [ ] 本日志已填写

## Git Commit

- Commit message：
- Pushed to GitHub：Yes / No
