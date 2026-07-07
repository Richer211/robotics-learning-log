# Week 2 Day 01 - ROS2 Environment Check

> 状态：**已完成** — ROS2 环境可用，workspace build 成功，publisher / subscriber 都能运行。

## Today's Goal

- [x] 在 Ubuntu VM 里确认 ROS2 Humble 环境
- [x] 克隆 / 进入仓库并构建 `week02_ros2_basics/ros2_ws`
- [x] 理解 ROS2 workspace、`source`、`colcon build`

## 1. 学（30 分钟）

阅读：

- [`../../week02_ros2_basics/README.md`](../../week02_ros2_basics/README.md)
- [`../environment.md`](../environment.md) 的 ROS2 Humble 安装和 workspace 部分

回答：

### ROS2 workspace 是什么？为什么有 `ros2_ws/src/`？

ROS2 workspace 是一个专门用来放 ROS2 package、统一 build 和运行的工作区。

本项目里的 workspace 是：

```text
week02_ros2_basics/ros2_ws
```

其中：

```text
ros2_ws/src/
```

是放 ROS2 源代码 package 的地方。本项目里的 ROS2 package 是：

```text
fake_sensor_pkg
```

也就是说，真正的代码在：

```text
week02_ros2_basics/ros2_ws/src/fake_sensor_pkg/fake_sensor_pkg/
```

里面的两个核心文件是：

- `distance_publisher.py`：发布假距离传感器数据
- `distance_subscriber.py`：接收假距离传感器数据

今天不需要深入理解这两个 Python 文件的每一行代码，只需要知道它们来自这个 package，并且通过 ROS2 topic 通信。后面 Day 02 / Day 03 再正式读代码。

### `source /opt/ros/humble/setup.bash` 是干什么的？

这条命令是让当前终端认识 ROS2 Humble。

可以简单理解成：

```text
告诉当前终端：ROS2 安装在这里，你现在可以使用 ros2、rclpy、sensor_msgs 等 ROS2 工具和库。
```

如果没有执行这条命令，终端可能不知道 `ros2` 命令和 ROS2 环境在哪里。

### `source install/setup.bash` 是干什么的？

这条命令是让当前终端认识自己刚刚 build 出来的 ROS2 package。

可以简单理解成：

```text
告诉当前终端：我刚刚 build 了 fake_sensor_pkg，你现在可以用 ros2 run 找到它。
```

如果新开一个终端但没有执行：

```bash
source install/setup.bash
```

运行时就会报：

```text
Package 'fake_sensor_pkg' not found
```

因为每个新终端都是新的 shell，它不会自动记住另一个终端里 source 过的环境。

### `colcon build --symlink-install` 和 Week 1 的 `cmake .. && make` 有什么相似点？

它们都是 build / 构建命令，作用都是把源代码整理成可以运行的程序或 package。

区别是：

- `cmake .. && make`：主要用于普通 C++ 项目。
- `colcon build --symlink-install`：用于 ROS2 workspace，可以一次构建 `src/` 下面的 ROS2 packages。

注意：build 不等于运行。

真正运行 ROS2 节点需要：

```bash
ros2 run fake_sensor_pkg distance_publisher
ros2 run fake_sensor_pkg distance_subscriber
```

## 2. 练（30 分钟）

在 Ubuntu VM 里执行：

```bash
source /opt/ros/humble/setup.bash
ros2 doctor
```

说明：

- `source /opt/ros/humble/setup.bash`：加载系统安装的 ROS2 Humble 环境。
- `ros2 doctor`：检查 ROS2 环境是否正常。本次结果显示 `All 5 checks passed`，说明 ROS2 环境可用。
- `ros2 --version` 不适合作为检查命令，因为 `ros2` 不支持 `--version` 参数，会报 `unrecognized arguments: --version`。这不是 ROS2 安装失败，而是命令参数不对。

如果还没把仓库放进 VM：

```bash
mkdir -p ~/robotics-learning-log
cd ~/robotics-learning-log
git clone https://github.com/Richer211/robotics-learning-log.git .
```

说明：

- `mkdir -p ~/robotics-learning-log`：在 VM 里创建项目文件夹。
- `cd ~/robotics-learning-log`：进入这个文件夹。
- `git clone ... .`：从 GitHub 下载仓库到当前目录。最后的 `.` 表示不要再多创建一层文件夹，直接把仓库内容放到当前目录。

我现在理解：VM 里的项目不是直接控制 macOS 的项目，而是在 Ubuntu VM 里通过 GitHub 重新下载了一份独立的仓库副本。

关系是：

```text
macOS 本地仓库  <--- push / pull --->  GitHub  <--- clone / pull --->  Ubuntu VM 仓库
```

然后构建：

```bash
cd ~/robotics-learning-log/week02_ros2_basics/ros2_ws
source /opt/ros/humble/setup.bash
colcon build --symlink-install
source install/setup.bash
```

说明：

- `cd ~/robotics-learning-log/week02_ros2_basics/ros2_ws`：进入 Week 2 的 ROS2 workspace。
- `source /opt/ros/humble/setup.bash`：让终端认识 ROS2 Humble。
- `colcon build --symlink-install`：构建 `ros2_ws/src/` 里的 ROS2 package。
- `source install/setup.bash`：让终端认识刚刚 build 出来的 `fake_sensor_pkg`。

构建成功后出现：

```text
Finished <<< fake_sensor_pkg
Summary: 1 package finished
```

说明 `fake_sensor_pkg` build 成功。

继续测试：

```bash
ros2 run fake_sensor_pkg distance_publisher
```

结果看到 `distance_publisher` 不断输出距离数据，说明 publisher 节点运行成功。

再开一个新终端时，需要重新执行：

```bash
cd ~/robotics-learning-log/week02_ros2_basics/ros2_ws
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 run fake_sensor_pkg distance_subscriber
```

这次 subscriber 成功运行，并且能收到 `/sensor/distance` 的距离数据。

## 3. 记中文笔记（10 分钟）

### ROS2 是否已安装成功？

是，ROS2 Humble 已经安装成功。

我运行 `ros2 doctor` 后看到：

```text
All 5 checks passed
```

这说明 ROS2 环境整体是正常的。

### `colcon build` 是否成功？

是，`colcon build --symlink-install` 成功。

终端显示：

```text
Finished <<< fake_sensor_pkg
Summary: 1 package finished
```

说明 `fake_sensor_pkg` 这个 ROS2 package 已经成功构建。

### 有无报错？如何解决？

今天遇到两个主要问题。

第一个问题是运行：

```bash
ros2 --version
```

报错：

```text
ros2: error: unrecognized arguments: --version
```

原因：`ros2` 命令不支持 `--version` 参数。这个错误不是 ROS2 没装好，而是检查命令写错了。

解决方式：用下面的命令检查：

```bash
ros2 doctor
ros2 --help
```

第二个问题是在新终端运行：

```bash
ros2 run fake_sensor_pkg distance_subscriber
```

报错：

```text
Package 'fake_sensor_pkg' not found
```

原因：新终端没有执行 `source install/setup.bash`，所以它还不认识刚刚 build 出来的 `fake_sensor_pkg`。

解决方式：每个新终端都先执行：

```bash
cd ~/robotics-learning-log/week02_ros2_basics/ros2_ws
source /opt/ros/humble/setup.bash
source install/setup.bash
```

然后再运行：

```bash
ros2 run fake_sensor_pkg distance_publisher
ros2 run fake_sensor_pkg distance_subscriber
```

### 今天我真正理解的过程

今天做的事情可以总结成：

```text
在 Ubuntu VM 里 clone GitHub 仓库
→ 进入 ROS2 workspace
→ 加载 ROS2 环境
→ build fake_sensor_pkg
→ 加载 workspace 环境
→ 运行 publisher 和 subscriber
```

更简单地说：

```text
我在 VM 里启动了一个最小 ROS2 假距离传感器系统。
```

其中：

- `distance_publisher` 是发布距离数据的节点。
- `/sensor/distance` 是传输距离数据的 topic。
- `distance_subscriber` 是接收距离数据的节点。

核心关系是：

```text
distance_publisher  --->  /sensor/distance  --->  distance_subscriber
```

## 4. English Summary + Key Terms（10 分钟）

写 3–5 句英文总结，并记录 Key Terms：

## English Summary

Today I checked my ROS2 Humble environment inside the Ubuntu VM.

I cloned the GitHub repository into the VM and built the ROS2 workspace with `colcon build --symlink-install`.

I learned that `source /opt/ros/humble/setup.bash` loads the ROS2 environment, and `source install/setup.bash` loads my own workspace package.

I also ran the fake distance publisher and subscriber successfully.

One important lesson is that every new terminal needs to source the workspace setup file before it can find `fake_sensor_pkg`.

| English | 中文 |
|---------|------|
| ROS2 workspace | ROS2 工作区 |
| colcon | ROS2 构建工具 |
| source | 加载环境脚本 |
| environment setup | 环境配置 |
| package | ROS2 包 |
| publisher | 发布者 |
| subscriber | 订阅者 |
| topic | 话题 / 数据频道 |
| setup file | 环境设置文件 |

## 60-second Speaking Draft

Today I checked my ROS2 environment inside the Ubuntu VM.

The goal was to build the Week 2 ROS2 workspace with `colcon`.

I learned that a ROS2 workspace contains packages under the `src` folder.

I cloned the project from GitHub into the VM and built the `fake_sensor_pkg` package.

I also learned that I need to source setup files before using ROS2 commands.

The publisher sends fake distance data, and the subscriber receives the data through the `/sensor/distance` topic.

If I open a new terminal, I need to run `source install/setup.bash` again, otherwise ROS2 cannot find my package.

## 完成标准

- [x] `ros2 doctor` 通过，或 `ros2 --help` 可运行
- [x] `colcon build --symlink-install` 成功
- [x] 能解释 `source` 的作用
- [x] `distance_publisher` 能运行
- [x] `distance_subscriber` 能运行
- [x] 本日志已填写

## Git Commit

- Commit message：
- Pushed to GitHub：No
