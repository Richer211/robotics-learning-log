# Week 2 日程表 — ROS2 Basics

每天打开 [`../CURRENT.md`](../CURRENT.md) 看「今天」是哪一天。Week 2 的代码主要在 **Ubuntu 22.04 VM** 里运行，笔记和 Git 仍在 macOS / Cursor 里维护。

| 天 | 主题 | 产出 | 日志 | 建议 Key Terms |
|----|------|------|------|----------------|
| Day 01 | ROS2 环境验证 + workspace build | `colcon build` 跑通 | `day01.md` | ROS2, workspace, colcon, source, environment |
| Day 02 | Node / Topic 基础 | publisher / subscriber 分开运行 | `day02.md` | node, topic, publisher, subscriber, message |
| Day 03 | 读懂 publisher / subscriber 代码 | 理解 `rclpy`、`Range`、callback | `day03.md` | rclpy, Range message, callback, timer, QoS |
| Day 04 | Launch file | 一条命令启动两个 node | `day04.md` | launch file, executable, package, output, process |
| Day 05 | rosbag | 录制和回放 `/sensor/distance` | `day05.md` | rosbag, record, playback, data logging, telemetry |
| Day 06 | 小改需求 + 重建 | 改阈值/频率并重新 build/run | `day06.md` | parameter, rebuild, warning threshold, iteration, debug |
| Day 07 | 周复盘 | Week 2 review + Week 3 准备 | `weekly-review-w02.md` | review, milestone, next steps, perception, pipeline |

## 每日英文（Week 2）

- **必做**：English Summary（3–5 句）+ Key Terms（3–8 个）→ 抄到 [`../glossary/robotics-terms.md`](../glossary/robotics-terms.md)
- **新增**：60-second Speaking Draft（可先读稿，不要求背诵）
- **暂不强求**：Interview Q&A（Week 3 起每周 2 次）

## Week 2 结束标准

- [ ] Ubuntu VM 可以稳定启动
- [ ] 能 `source /opt/ros/humble/setup.bash`
- [ ] `week02_ros2_basics/ros2_ws` 能 `colcon build --symlink-install`
- [ ] 能运行 publisher / subscriber
- [ ] 能用 `ros2 topic list`、`ros2 topic echo`、`ros2 node list` 观察系统
- [ ] 能用 launch file 一次启动两个 node
- [ ] 能录制和回放 rosbag
- [ ] 能用英文简单解释 node / topic / publisher / subscriber

## Week 2 学习原则

- 先跑通，再解释，再修改。
- ROS2 命令全部在 Ubuntu VM 里运行。
- Git commit 仍在 macOS 仓库里完成；如果 VM 里改代码，注意同步回仓库。
