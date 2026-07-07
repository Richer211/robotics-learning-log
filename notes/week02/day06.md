# Week 2 Day 06 - Modify ROS2 Demo Requirement

> 状态：**未开始**

## Today's Goal

- [ ] 对 Week 2 ROS2 demo 做一个小改动
- [ ] 重新 build / source / run
- [ ] 理解「改代码 → 重建 → 运行验证」的迭代流程

## 1. 学（20 分钟）

回顾：

- Week 1 Python/C++ 中的 `WARNING_DISTANCE_M`
- Week 2 publisher / subscriber 中的 `WARNING_DISTANCE_M`
- `colcon build --symlink-install` 后为什么还要 `source install/setup.bash`

回答：

- publisher 和 subscriber 里都有 warning threshold，会不会不一致？
- 如果只改 subscriber，系统行为会怎么变化？
- 如果改 publisher 的 timer 从 `0.5` 到 `0.2`，输出频率会怎么变化？

## 2. 练（40 分钟）

任选一个小改动：

- 把 warning threshold 从 `1.0` 改成 `0.8`
- 把 publisher 的 timer 从 `0.5` 改成 `0.2`
- 修改日志输出，让它更容易读

修改后在 Ubuntu VM 中重新执行：

```bash
cd ~/robotics-learning-log/week02_ros2_basics/ros2_ws
source /opt/ros/humble/setup.bash
colcon build --symlink-install
source install/setup.bash
ros2 launch fake_sensor_pkg sensor_demo.launch.py
```

记录修改前后有什么差异。

## 3. 记中文笔记（10 分钟）

- 今天改了哪一行？
- 为什么要重新 build / source？
- 修改后的现象是否符合预期？
- 遇到的报错和解决方式是什么？

## 4. English Summary + Key Terms（10 分钟）

| English | 中文 |
|---------|------|
| warning threshold | 警告阈值 |
| publish rate | 发布频率 |
| rebuild | 重新构建 |
| iteration | 迭代 |
| debug | 调试 |

## 60-second Speaking Draft

Today I modified the ROS2 fake sensor demo and tested the result.

I changed one small requirement, rebuilt the workspace, and ran the launch file again.

This helped me understand the normal robotics development loop: edit code, build, source, run, and verify.

I also learned that small parameter changes can change the runtime behavior of a ROS2 node.

## 完成标准

- [ ] 完成一个小改动
- [ ] 重新 build 成功
- [ ] 运行后观察到改动效果
- [ ] 本日志已填写

## Git Commit

- Commit message：
- Pushed to GitHub：Yes / No
