# Day 01 - Robotics Learning

## Today's Goal

- Create robotics-learning folder
- Create GitHub repository
- Run Python fake sensor demo
- Run C++ fake sensor demo with CMake

## What I Finished

- [x] Created robotics-learning project folder
- [x] Created GitHub repository
- [x] Wrote and ran Python fake sensor simulation
- [x] Wrote and ran C++ fake sensor simulation
- [x] Built C++ project with CMake

---

## 中文总结

今天搭建了机器人学习仓库，并用 Python 和 C++ 各写了一个假距离传感器 demo。

核心收获：机器人软件常遵循「持续读取传感器数据 → 处理 → 输出结果」的模式；C++ 需要 CMake 构建才能生成可执行文件。

还不懂：CMake 每一行的具体含义（后续继续学）。

## English Summary

Today I built two simple fake distance sensor demos.

The first version was written in Python, and the second version was written in C++.

The goal was to simulate continuous sensor readings in a robotics system.

I also used CMake to build the C++ project.

The main thing I learned was a basic robotics software pattern: read sensor data, process it, and print the result.

One problem I had was that C++ needs more setup than Python.

Tomorrow I plan to review Linux commands and Git workflow.

## Key Terms

| English | 中文 |
|---------|------|
| distance sensor | 距离传感器 |
| sensor reading | 传感器读数 |
| simulation | 模拟 |
| CMake | C++ 项目构建工具 |
| executable | 可执行文件 |
| build process | 编译构建流程 |
| continuous data | 连续数据 |
| safety threshold | 安全阈值 |

（完整词汇见 [`glossary/robotics-terms.md`](glossary/robotics-terms.md)）

## 60-second Speaking Draft

Today I worked on a fake distance sensor demo.

I wrote one version in Python and another version in C++.

The program generates random distance values to simulate sensor readings.

In a real robot, sensors continuously collect data from the environment.

This demo is very simple, but it helps me understand the basic idea of robotics software.

I also used CMake to build the C++ version, so I practiced the basic C++ build process.

Tomorrow, I plan to review Linux commands, Git workflow, and basic C++ classes.

## Interview Practice

**Q: What did you build today?**

A: I built a simple fake distance sensor demo in both Python and C++.

**Q: Why did you build it?**

A: I built it to understand how robotics software can simulate continuous sensor readings.

**Q: What did you learn from this demo?**

A: I learned that a basic robotics program often follows a loop: read data, process data, and output a result.

**Q: Why did you use CMake?**

A: I used CMake to manage the C++ build process and generate an executable.

---

## What I Learned

- Python can quickly simulate simple sensor data.
- C++ needs a build process, and CMake helps manage compilation.
- Robotics software often uses both Python and C++.
- A robot program usually receives continuous sensor-like data, processes it, and outputs results.

## Problems I Met

- C++ needs more setup than Python.
- I need to become more familiar with CMake and folder structure.

## Notes

Today's fake sensor demo is simple, but it represents a basic robotics idea:

> A robot continuously receives sensor data from the real world.

## Tomorrow's Plan

- Review basic Linux commands
- Review Git workflow
- Continue C++ / CMake practice
- Prepare for ROS2 environment setup

## Git Commit

- Commit message: `Day 01 fake sensor demos and learning log`
- Pushed to GitHub: Yes
