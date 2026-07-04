# Day 06 - Robotics Learning

> 状态：**进行中** — Ubuntu VM 正在安装。

## Today's Goal

- [x] `docker run hello-world`（如已装 Docker）
- [x] 阅读并按步骤开始 `notes/environment.md` 的 VM 安装
- [x] 下载 UTM 和 Ubuntu 22.04 ARM64 ISO，并创建 Ubuntu VM

## What I Finished

- [x] 阅读 `[notes/environment.md](environment.md)`，理解 macOS / Ubuntu VM / Docker 的分工
- [x] 运行 Docker hello-world，并看到 `Hello from Docker!`
- [x] 下载 UTM 和 Ubuntu 22.04.5 live-server ARM64 ISO
- [x] 在 UTM 中创建 `Ubuntu 22.04 ROS2` 虚拟机（8 GB RAM、4 CPU cores、64 GB storage）
- [x] 启动 Ubuntu Server 安装流程，安装 OpenSSH Server

## What I Learned（中文）

### 为什么 Week 1 在 macOS 写代码，Week 2+ 要用 Ubuntu VM 跑 ROS2？

- Week 1 主要学习 Python、C++、Linux 命令、Git、CMake 等基础内容，这些可以直接在 macOS 上完成。
- Week 2 开始要学习 ROS2 Humble、RViz、Gazebo、rosbag 等工具。ROS2 Humble 官方主要支持 Ubuntu 22.04，在 Ubuntu VM 中安装和运行最稳定，也更符合教程环境。



### UTM + Ubuntu 22.04 和 Docker 各自解决什么问题？

- **UTM + Ubuntu 22.04**：提供一个完整的 Linux 虚拟机环境，适合安装 ROS2、RViz、Gazebo 等需要完整 Ubuntu 系统的工具。
- **Docker**：提供轻量级容器，用于环境隔离和复现。它适合快速运行命令或服务，但不是完整桌面系统；直接跑 RViz / Gazebo 图形界面不如 VM 方便。



### VM 推荐配置是多少？

- RAM：8 GB minimum
- Disk：40 GB minimum（本次设置 64 GB）
- CPU：4 cores if available



### ROS2 Humble / VM / UTM 的理解

- ROS2 Humble 是机器人软件框架，主要运行在 Ubuntu 22.04 上。
- RViz 用来可视化机器人和传感器数据；Gazebo 用来做仿真；rosbag 用来录制和回放 ROS2 数据；colcon 用来构建 ROS2 工作区。
- UTM 是 macOS 上运行虚拟机的软件；ISO 是 Ubuntu 的安装盘镜像；真正的 Linux 系统是安装到虚拟硬盘里的 Ubuntu 22.04.5 LTS。
- 从 Week 2 开始，ROS2 相关学习主要在 Ubuntu VM 里进行；macOS / Cursor 继续用于写笔记、管理 Git 和阅读代码。
- 当前先安装 Ubuntu Server，再安装 `ubuntu-desktop`，是为了后面能更方便地使用 RViz 和 Gazebo 等图形工具。



### Week 2 仓库代码在 VM 里怎么拉、怎么 `colcon build`？

```bash
mkdir -p ~/robotics-learning-log
cd ~/robotics-learning-log
git clone https://github.com/Richer211/robotics-learning-log.git .
cd week02_ros2_basics/ros2_ws
colcon build
source install/setup.bash
```

- `git clone ... .` 里的 `.` 表示把仓库克隆到当前目录，避免多嵌套一层目录。
- `colcon build` 是 ROS2 的构建命令，会把 `ros2_ws/src/` 里的包编译成可运行节点。
- `source install/setup.bash` 会让当前终端认识刚刚构建好的 ROS2 包；每个新终端都要 source 一次，或之后写进 `~/.bashrc`。



### macOS / Ubuntu VM / Docker 在学习路径里的角色

- **macOS**：日常写代码、提交 Git、学习 Python / C++ / 文档。
- **Ubuntu VM**：运行 ROS2 Humble、RViz、Gazebo、rosbag，是 Week 2 之后的主要机器人开发环境。
- **Docker**：用于轻量级环境隔离和复现，可作为辅助工具，但不替代 Ubuntu 桌面 VM。



### ROS2 Humble 为什么装在 VM 里而不是 macOS 原生？

- ROS2 Humble 的主流支持环境是 Ubuntu 22.04。
- RViz、Gazebo、rosbag、colcon 等 ROS2 工具在 Ubuntu 上最稳定，教程和社区资料也基本按 Ubuntu 编写。



### `environment.md` 底部 Verification Checklist 有哪些验收项？

1. macOS: `python3 --version`, `cmake --version`, `git --version`
2. VM: `lsb_release -a` shows Ubuntu 22.04
3. VM: `ros2 doctor` passes
4. VM: `colcon build` succeeds in `week02_ros2_basics/ros2_ws`
5. Docker: `docker run hello-world`



## Practice Log



### Docker

```bash
docker run hello-world
```

- 运行成功，看到 `Hello from Docker!`



### Ubuntu VM

- 已下载 UTM
- 已下载 `ubuntu-22.04.5-live-server-arm64.iso`
- 已创建 UTM 虚拟机：`Ubuntu 22.04 ROS2`
- 配置：ARM64 / 8 GB RAM / 4 CPU cores / 64 GB storage
- 已开始安装 Ubuntu Server，并安装 OpenSSH Server
- Ubuntu Server 安装完成，已移除 ISO 并成功登录。
- 系统版本：Ubuntu 22.04.5 LTS (Jammy)
- 已运行 `sudo apt update`
- OpenSSH Server 状态：active (running)
- Ubuntu Desktop 安装完成，已成功进入图形桌面。
- VM IP：192.168.64.6。
- OpenSSH Server 已启用，状态为 active (running)。



## English Summary

Today I set up the Ubuntu virtual machine for my ROS2 learning environment.

I learned that macOS is good for daily coding and Git, while Ubuntu VM is better for ROS2, RViz, Gazebo, and rosbag.

I ran Docker hello-world successfully, installed Ubuntu 22.04.5 LTS ARM64 in UTM, and then installed the Ubuntu Desktop environment.

The VM uses 8 GB RAM, 4 CPU cores, and 64 GB storage. I also verified that SSH is active and the VM IP address is `192.168.64.6`.

Tomorrow I will review Week 1 and prepare the Ubuntu VM for ROS2 Humble.

## Key Terms


| English                 | 中文                     |
| ----------------------- | ---------------------- |
| virtual machine         | 虚拟机                    |
| Ubuntu                  | Linux 发行版              |
| container               | 容器                     |
| Docker                  | 容器工具                   |
| ROS2                    | 机器人操作系统第二代             |
| development environment | 开发环境                   |
| ARM64                   | Apple Silicon / ARM 架构 |
| ISO image               | 系统安装镜像                 |
| SSH                     | 远程登录协议                 |
| OpenSSH Server          | SSH 服务端，用于远程登录 VM      |
| Ubuntu Desktop          | Ubuntu 图形桌面环境          |
| colcon build            | ROS2 工作区构建命令           |




## Tomorrow's Plan

1. 填写 Week 1 周复盘
2. 记录 Ubuntu VM 安装结果和配置
3. 准备开始 ROS2 Humble 安装步骤



## Git Commit

- Commit message：Day 06: set up Ubuntu VM for ROS2"
- Pushed to GitHub：Yes 

