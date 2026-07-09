# Week 2 Day 04 - ROS2 Launch File

> 状态：**已完成** — 已用 launch file 一次启动 publisher 和 subscriber，并用 `ros2 node list` 验证两个节点。

## Today's Goal

- [x] 理解 launch file 的作用
- [x] 使用一条命令同时启动 publisher 和 subscriber
- [x] 读懂 `sensor_demo.launch.py`

## 1. 学（30 分钟）

阅读：

- `week02_ros2_basics/ros2_ws/src/fake_sensor_pkg/launch/sensor_demo.launch.py`
- [`../../week02_ros2_basics/README.md`](../../week02_ros2_basics/README.md) 的 Launch 部分

回答：

- launch file 解决什么问题？

launch file 用来一次启动和管理多个 ROS2 node。

它解决的问题是：不用手动开多个终端分别运行节点。真实机器人系统里通常会有很多 node，如果每个都手动运行，会很麻烦，也容易出错。

- `Node(package=..., executable=..., name=..., output='screen')` 每个字段是什么意思？

1. `package`：ROS2 包名，不是文件压缩包。本项目里是 `fake_sensor_pkg`。
2. `executable`：可执行入口，也就是要启动的程序。本项目里是 `distance_publisher` 和 `distance_subscriber`。
3. `name`：运行时 node 的名字。启动后可以在 `ros2 node list` 里看到 `/distance_publisher` 和 `/distance_subscriber`。
4. `output='screen'`：把节点日志输出到当前终端屏幕上，方便观察运行状态。

对应到 `sensor_demo.launch.py`：

```python
Node(
  package='fake_sensor_pkg',
  executable='distance_publisher',
  name='distance_publisher',
  output='screen',
)
```

意思是：从 `fake_sensor_pkg` 这个 ROS2 package 里启动 `distance_publisher` 这个可执行入口，并把运行时 node 命名为 `distance_publisher`，日志输出到屏幕。

- launch 和手动开两个终端运行有什么区别？

手动运行时，需要分别开两个终端：

```bash
ros2 run fake_sensor_pkg distance_publisher
ros2 run fake_sensor_pkg distance_subscriber
```

launch 运行时，只需要一条命令：

```bash
ros2 launch fake_sensor_pkg sensor_demo.launch.py
```

launch file 更适合真实机器人系统，因为真实系统通常需要同时启动多个 node，并统一管理启动配置和日志输出。

## 2. 练（30 分钟）

在 Ubuntu VM 中执行：

```bash
cd ~/robotics-learning-log/week02_ros2_basics/ros2_ws
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 launch fake_sensor_pkg sensor_demo.launch.py
```
```bash
richard@ubuntu-ros2:~/robotics-learning-log/week02_ros2_basics/ros2_ws$ ros2 launch fake_sensor_pkg sensor_demo.launch.py
[INFO] [launch]: All log files can be found below /home/richard/.ros/log/2026-07-09-17-25-26-683567-ubuntu-ros2-27797
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [distance_publisher-1]: process started with pid [27798]
[INFO] [distance_subscriber-2]: process started with pid [27800]
[distance_publisher-1] [INFO] [1783617927.102596216] [distance_publisher]: Distance publisher started on /sensor/distance
[distance_subscriber-2] [INFO] [1783617927.102959794] [distance_subscriber]: Distance subscriber listening on /sensor/distance
[distance_publisher-1] [INFO] [1783617927.601270502] [distance_publisher]: Frame 0: distance=3.30 m
[distance_subscriber-2] [INFO] [1783617927.601723796] [distance_subscriber]: [1] distance=3.30 m
[distance_publisher-1] [INFO] [1783617928.099222579] [distance_publisher]: Frame 1: distance=1.40 m
[distance_subscriber-2] [INFO] [1783617928.099538777] [distance_subscriber]: [2] distance=1.40 m
[distance_publisher-1] [WARN] [1783617928.598838281] [distance_publisher]: Frame 2: close obstacle at 0.92 m
```

另开一个终端观察：

```bash
source /opt/ros/humble/setup.bash
source ~/robotics-learning-log/week02_ros2_basics/ros2_ws/install/setup.bash
ros2 node list
ros2 topic list
```
```bash
richard@ubuntu-ros2:~/robotics-learning-log/week02_ros2_basics/ros2_ws$ ros2 node list

/distance_publisher
/distance_subscriber
richard@ubuntu-ros2:~/robotics-learning-log/week02_ros2_basics/ros2_ws$ ros2 topic list

/parameter_events
/rosout
/sensor/distance
```

## 3. 记中文笔记（10 分钟）

- launch file 和手动运行两个节点的差异

launch file 可以在一个终端里同时启动 publisher 和 subscriber 两个节点。

手动运行则需要在两个终端里分别运行 publisher 节点和 subscriber 节点。

更重要的是，launch file 不只是“少开终端”，它还可以统一管理多个 node 的启动方式、名字、参数和输出。

- `output='screen'` 的作用

`output='screen'` 表示把节点日志直接打印到当前终端屏幕上。

这样运行 `ros2 launch` 时，可以同时看到：

- publisher 的输出
- subscriber 的输出
- launch 系统自己的日志

- 什么时候需要 launch file？

当一个机器人系统需要同时启动多个 node，或者需要统一管理启动配置时，就适合使用 launch file。

真实机器人系统通常会有很多节点，比如传感器节点、定位节点、控制节点、可视化节点等，不可能每次都手动开很多终端启动。

## 4. English Summary + Key Terms（10 分钟）

## English Summary

Today I learned how to use a ROS2 launch file.

The launch file starts both the distance publisher and the distance subscriber with one command.

I learned that `package` means the ROS2 package name, and `executable` means the program entry point that ROS2 can run.

I also learned that `output='screen'` sends node logs to the terminal, which helps me observe the running system.

I used `ros2 node list` to verify that both nodes were running.

| English | 中文 |
|---------|------|
| launch file | 启动文件 |
| executable | 可执行入口 |
| package | ROS2 包 |
| process | 进程 |
| output | 输出 |
| launch system | 启动系统 |
| node name | 节点名称 |
| screen output | 屏幕输出 |

## 60-second Speaking Draft

Today I learned how to use a ROS2 launch file.

The launch file starts both the distance publisher and the distance subscriber with one command.

This is useful because real robot systems often need many nodes to run together.

I also used `ros2 node list` and `ros2 topic list` to verify that the nodes were running.

## 完成标准

- [x] `ros2 launch fake_sensor_pkg sensor_demo.launch.py` 成功
- [x] 能解释 `sensor_demo.launch.py`
- [x] 能用 `ros2 node list` 验证两个节点
- [x] 本日志已填写

## Git Commit

- Commit message：learn day04
- Pushed to GitHub：Yes
