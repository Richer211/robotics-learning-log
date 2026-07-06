# Day 07 - Robotics Learning

> 状态：**已完成**

## Today's Goal

- [x] 填写 Week 1 周复盘
- [x] 验证 UTM + Ubuntu 22.04 VM 状态
- [x] 通过 SSH 从 macOS 连接 Ubuntu VM

## What I Finished

- [x] 完成 Week 1 学习复盘
- [x] 验证 Ubuntu VM：Ubuntu 22.04.5 LTS、IP、SSH
- [x] 从 macOS 成功 SSH 连接到 Ubuntu VM

### Week 1 你真正完成了哪些可运行产出？

- 完成了 Python 和 C++ 两个 `FakeSensor` demo，用随机距离模拟距离传感器读数，并根据阈值输出 `OK` / `WARNING`。
- 创建并维护 `Robotics Learning` 仓库，持续用 Git commit / push 记录学习进度。
- 修改过告警距离，并使用固定随机种子对比不同阈值下的输出结果。
- 学习了 `.gitignore`、README 构建流程、CMake 编译流程和 Git diff / staged / rm 等常用操作。
- 安装 Docker，完成 `docker run hello-world`。
- 安装 UTM + Ubuntu 22.04.5 VM，并从 macOS 成功 SSH 连接到 VM。

### 你现在最熟的 3 个技能是什么？

- Git 基础工作流：`status` / `diff` / `add` / `commit` / `push` / `log`
- Linux 基础命令：`cd` / `ls` / `grep` / `echo` / `cat` / `rm`
- CMake 项目基本构建流程：`cmake ..`、`make`、运行可执行文件

### 你还不熟、Week 2 需要继续练的 3 个点是什么？

- Python 和 C++ 还需要更多手写练习，不能只停留在读懂代码。
- ROS2 的 node、topic、publisher、subscriber 还不了解，需要 Week 2 从最小 demo 开始。
- 需要熟悉在 Ubuntu VM 里使用终端、Git、colcon、ROS2 命令来构建和运行代码。

### Ubuntu VM 现在是否足够支撑 Week 2 学 ROS2？

- 是的，足够支持。
- VM 已安装 Ubuntu 22.04.5 LTS，并成功进入图形桌面。
- VM IP：`192.168.64.6`
- SSH：从 macOS 成功连接 `ssh richard@192.168.64.6`

## English Summary

Today I reviewed everything I completed in Week 1.

I built and studied Python and C++ fake sensor demos, practiced Linux and Git commands, and learned the basic CMake build workflow.

I also set up the Ubuntu 22.04 VM for ROS2 and connected to it from macOS using SSH.

The main thing I still need to practice is writing Python and C++ code by myself, not only reading and modifying existing code.

Next week I will start ROS2 basics with nodes, topics, publishers, and subscribers.

## Key Terms

| English | 中文 |
|---------|------|
| weekly review | 周复盘 |
| milestone | 阶段性成果 |
| SSH connection | SSH 连接 |
| ROS2 setup | ROS2 环境配置 |
| next steps | 下一步计划 |
| publisher | 发布者节点 |
| subscriber | 订阅者节点 |
| topic | ROS2 话题 |

## Git Commit

- Commit message：
- Pushed to GitHub：Yes / No
