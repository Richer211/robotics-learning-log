# Week 01 Review

> 状态：**已完成** — Day 07 填写。

## What did I complete this week?

- 学习了 Linux basic commands 和 Git commands，并完成 Day 02 的扩展练习。
- 创建了 `Robotics Learning` 项目并持续提交到 GitHub。
- 分别运行和理解了 Python / C++ `FakeSensor` demos（不是完全自己从零写的，但已逐行理解并修改过）。
- 学习了 Python class、C++ class、`.hpp` / `.cpp` 分工、CMake 编译流程。
- 理解了 `.gitignore` 的作用，以及为什么 `build/`、`.DS_Store`、`__pycache__/`、日志和二进制文件不应该提交到 GitHub。
- 安装 Docker，并成功运行 `docker run hello-world`。
- 安装 UTM + Ubuntu 22.04.5 VM，进入 Ubuntu Desktop，并从 macOS 通过 SSH 成功连接。
- 理解了 Docker、UTM、Ubuntu VM 的区别，以及为什么 ROS2 Humble 主要在 Ubuntu VM 中运行。

## Main problems encountered?

- Python 和 C++ 的手写经验还很少，目前更多是理解、运行、修改已有代码。
- 对 ROS2 的 node、topic、publisher、subscriber 还不了解。
- 对环境搭建、虚拟机、SSH、ROS2 工具链还不熟悉，需要 Week 2 继续练。
- 对 C++ 的 class、构造函数、`private`、`const`、随机数引擎等概念需要继续复习。


## Bugs I solved?

- 修正了 `git diff` / `git diff --staged` 的理解，知道了工作区、暂存区、上次 commit 的区别。
- 学会处理 `git rm` 报错，理解未跟踪文件、已暂存文件和已跟踪文件的删除方式。
- 修正了 `.gitignore` 的注释写法，知道 `.gitignore` 规则不能写成 `build/ # comment` 这种形式。
- 在 Python 代码中使用 `random.seed(42)`，在 C++ 代码中使用 `sensor.seed(42)`，用于固定随机序列并比较不同 `WARNING_DISTANCE_M` 的输出。
- 完成 UTM + Ubuntu 22.04.5 安装，解决 ISO 启动盘未移除导致的启动问题。


## What do I still not understand?

- 对 C++ 的结构化文件、声明、实现、构造函数、成员变量和 `const` 还需要更多练习。
- 对 SSH、`colcon build`、ROS2 workspace、node、topic、publisher、subscriber 还不了解。
- 对如何在 Ubuntu VM 中完整开发、构建、运行、调试 ROS2 项目还不熟悉。

## Top 3 tasks for next week

1. 最小化实现一个ROS2 Humble demo
2. 理解并运行 ROS2 topic / node / publisher / subscriber 的基础命令
3. 在学习 Week 2 demo 后，尝试模仿重写一个最小 publisher / subscriber

## Am I on track for target roles?

- Robotics Software Engineer：Yes 
- Robotics Perception Engineer：Yes（还在早期，Week 3/4 会更相关）
- Robotics Simulation Engineer：Yes（已开始准备 Ubuntu VM / ROS2 环境）
- Robotics Integration Engineer：Not yet（后续 ROS2 + Git + 环境配置会逐步靠近）

## English Summary

This week I completed the foundation stage of my robotics learning plan.

I practiced Linux and Git, studied Python and C++ fake sensor demos, and learned the basic CMake build workflow.

I also set up the Ubuntu 22.04 VM for ROS2 and verified SSH access from macOS.

My main weakness is that I still need more practice writing Python and C++ code from scratch.

Next week I will start ROS2 basics by running a minimal publisher and subscriber demo.
