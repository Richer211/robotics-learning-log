# Robotics & Engineering Glossary

英中对照词汇表。每天从当日日志 **Key Terms** 抄录新词；每周读 1 份英文 JD 时把不懂的词也加进来。

**规则：**
- 只记当天真正用到的词，不堆砌
- 格式：`| English term | 中文 | 简短例句或备注 |`
- Week 1 目标：约 40–50 词；Month 1 目标：约 80 词

---

## Day 01 — Fake Distance Sensor Demo

| English | 中文 | Note |
|---------|------|------|
| distance sensor | 距离传感器 | Measures how far an object is |
| sensor reading | 传感器读数 | A single measurement from a sensor |
| simulation | 模拟 | Fake data instead of real hardware |
| random distance value | 随机距离值 | Used in our fake sensor demo |
| CMake | C++ 构建工具 | Generates build files for C++ |
| executable | 可执行文件 | `./fake_sensor` after `make` |
| build process | 编译构建流程 | configure → compile → link → run |
| continuous data | 连续数据 | Sensors stream readings over time |
| safety threshold | 安全阈值 | Distance below which we warn |
| obstacle detection | 障碍物检测 | Detecting objects in the robot's path |

---

## Day 02 — Linux & Git

| English | 中文 | Note |
|---------|------|------|
| terminal | 终端 | Command-line interface for Linux |
| working directory | 工作目录 | Current folder (`pwd` shows it) |
| redirect | 重定向 | `>` overwrite file, `>>` append |
| grep | 搜索文件内容 | Find text inside files |
| git status | 查看 Git 状态 | Shows modified / staged / untracked files |
| staging area | 暂存区 | After `git add`, before `git commit` |
| git diff | 查看未暂存改动 | Compares working tree vs staging area |
| git diff --staged | 查看已暂存改动 | Compares staging area vs last commit |
| commit | 提交 | Save a snapshot to Git history |
| HEAD | 当前提交指针 | Not a command — marks where you are |

---

## Day 03 — Python Class

| English | 中文 | Note |
|---------|------|------|
| class | 类 | Groups data and methods together |
| constructor | 构造函数 | Python: `__init__`; sets up the object |
| method | 方法 | A function inside a class |
| warning threshold | 告警阈值 | Distance below which status = WARNING |
| random seed | 随机种子 | Same seed → same random sequence |
| command-line argument | 命令行参数 | e.g. `--frames 10 --interval 0.5` |
| sensor simulation | 传感器模拟 | Fake readings without real hardware |
| parse | 解析 | Read and interpret CLI arguments |

---

## Day 04 — C++ Class

| English | 中文 | Note |
|---------|------|------|
| header file | 头文件 | `.hpp` — declares classes and methods |
| source file | 源文件 | `.cpp` — implements the logic |
| declaration | 声明 | What exists (signatures, members) |
| implementation | 实现 | How methods actually work |
| compile | 编译 | Turn source code into machine code |
| link | 链接 | Combine `.o` files into one executable |
| encapsulation | 封装 | Hide internals with `private` |
| member variable | 成员变量 | Object state, e.g. `gen_` |
| const member function | 常量成员函数 | Promises not to modify object state |
| random engine | 随机引擎 | e.g. `std::mt19937` in our sensor |

---

## Day 05 — Repo Hygiene

| English | 中文 | Note |
|---------|------|------|
| gitignore | Git 忽略规则文件 | Tells Git which files not to track |
| build artifact | 编译产物 | e.g. `build/`, compiled binaries |
| source code | 源代码 | Human-readable `.py`, `.cpp`, `.hpp` files |
| repository | 代码仓库 | This project's GitHub repo |
| README | 项目说明文档 | How to build and run the project |
| version control | 版本控制 | Managing code changes with Git |
| regenerate | 重新生成 | Logs and build outputs can be recreated |
| metadata | 元数据 | e.g. `.DS_Store` — not project source code |

---

## Day 06 — Environment Setup

| English | 中文 | Note |
|---------|------|------|
| virtual machine | 虚拟机 | Runs Ubuntu inside macOS |
| Ubuntu | Linux 发行版 | Main OS for ROS2 Humble |
| container | 容器 | Lightweight isolated environment |
| Docker | 容器工具 | Used for reproducible environments |
| ROS2 | 机器人操作系统第二代 | Robot software framework |
| development environment | 开发环境 | Tools and OS used for coding/running projects |
| ARM64 | ARM 架构 | Apple Silicon / M1 architecture |
| ISO image | 系统安装镜像 | Installer image for Ubuntu |
| SSH | 远程登录协议 | Used to connect to the VM from macOS |
| OpenSSH Server | SSH 服务端 | Allows remote login into the VM |
| Ubuntu Desktop | Ubuntu 图形桌面环境 | Needed for GUI tools like RViz / Gazebo |
| colcon build | ROS2 工作区构建命令 | Builds ROS2 packages in a workspace |

---

## Day 07 — Week 1 Review

| English | 中文 | Note |
|---------|------|------|
| weekly review | 周复盘 | Review what was completed during the week |
| milestone | 阶段性成果 | A meaningful checkpoint in the learning plan |
| SSH connection | SSH 连接 | Remote terminal access from macOS to Ubuntu VM |
| ROS2 setup | ROS2 环境配置 | Preparing Ubuntu VM for ROS2 Humble |
| next steps | 下一步计划 | Tasks to start in Week 2 |
| publisher | 发布者节点 | Sends messages to a ROS2 topic |
| subscriber | 订阅者节点 | Receives messages from a ROS2 topic |
| topic | ROS2 话题 | Named communication channel between nodes |

---

## Week 2 Day 01 — ROS2 Environment Check

| English | 中文 | Note |
|---------|------|------|
| ROS2 workspace | ROS2 工作区 | Folder used to build and run ROS2 packages |
| colcon | ROS2 构建工具 | Builds packages inside a ROS2 workspace |
| source | 加载环境脚本 | Makes the current terminal know ROS2 or local packages |
| setup file | 环境设置文件 | e.g. `setup.bash`, loaded with `source` |
| environment setup | 环境配置 | Preparing Ubuntu VM and ROS2 tools |
| package | ROS2 包 | A unit of ROS2 code, e.g. `fake_sensor_pkg` |
| publisher | 发布者节点 | Sends fake distance messages to a topic |
| subscriber | 订阅者节点 | Receives fake distance messages from a topic |
| topic | 话题 / 数据频道 | Named channel such as `/sensor/distance` |
| clone | 克隆仓库 | Download a GitHub repository into the VM |

---

## Week 2 Day 02 — ROS2 Node / Topic Basics

| English | 中文 | Note |
|---------|------|------|
| node | 节点 | A running ROS2 program or module |
| topic | 话题 / 数据频道 | Communication channel between nodes |
| publisher | 发布者节点 | Sends messages to a topic |
| subscriber | 订阅者节点 | Receives messages from a topic |
| message | 消息 | Structured data sent through a topic |
| Range message | 距离范围消息 | `sensor_msgs/Range` used for distance readings |
| frame_id | 坐标系/传感器框架 ID | Identifies the sensor frame, e.g. `fake_lidar_link` |
| topic echo | 输出 topic 消息内容 | `ros2 topic echo /sensor/distance` prints live messages |
| node list | 节点列表 | `ros2 node list` shows running ROS2 nodes |

---

## Week 2 Day 04 — ROS2 Launch File

| English | 中文 | Note |
|---------|------|------|
| launch file | 启动文件 | Starts one or more ROS2 nodes with one command |
| launch system | 启动系统 | ROS2 system for starting and managing nodes |
| executable | 可执行入口 | Program entry point started by `ros2 run` or `ros2 launch` |
| package | ROS2 包 | A ROS2 code unit such as `fake_sensor_pkg` |
| node name | 节点名称 | Runtime name shown by `ros2 node list` |
| process | 进程 | A running program in the operating system |
| output | 输出 | Logs or messages printed by a node |
| screen output | 屏幕输出 | Logs printed directly to the terminal |

---

## Week 2 Day 05 — ROS2 Bag Record / Playback

| English | 中文 | Note |
|---------|------|------|
| rosbag | ROS 数据包工具 | Records and replays ROS2 topic messages |
| record | 录制 | Save live topic messages into a bag file |
| playback | 回放 | Play recorded topic messages again |
| replay | 重新播放 | Publish saved messages again in time order |
| bag file | 数据包文件 | Stored rosbag data, e.g. `.db3` file |
| metadata | 元信息 | Bag information such as topics, types, and duration |
| telemetry | 遥测/运行数据 | Runtime data from sensors or systems |
| data logging | 数据记录 | Saving data for later analysis and debugging |
| offline debugging | 离线调试 | Debugging with recorded data instead of a live robot |

---

## JD Vocabulary（从招聘启事积累）

| English | 中文 | Source |
|---------|------|--------|
| | | |
