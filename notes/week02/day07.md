# Week 2 Day 07 - Review and Prepare for Week 3

> 状态：**未开始**

## Today's Goal

- [ ] 完成 Week 2 复盘
- [ ] 整理 ROS2 基础概念
- [ ] 更新 glossary
- [ ] 准备 Week 3 perception / vision 学习

## 1. 回顾（30 分钟）

检查 Week 2 是否完成：

- [ ] ROS2 Humble 环境可用
- [ ] `colcon build --symlink-install` 成功
- [ ] publisher / subscriber 可以分开运行
- [ ] launch file 可以一键启动
- [ ] rosbag 可以录制和回放
- [ ] 至少完成一次小改动并验证

## 2. 复盘问题（30 分钟）

写在 [`weekly-review-w02.md`](weekly-review-w02.md)：

- Week 2 最重要的 3 个收获是什么？
- ROS2 里 node / topic / publisher / subscriber 的关系是什么？
- `colcon build`、`source install/setup.bash`、`ros2 run`、`ros2 launch` 的流程是什么？
- rosbag 为什么重要？
- 还有哪些概念不清楚？

## 3. English Summary + Key Terms（10 分钟）

整理 Week 2 Key Terms，并同步到 [`../glossary/robotics-terms.md`](../glossary/robotics-terms.md)：

| English | 中文 |
|---------|------|
| ROS2 node | ROS2 节点 |
| topic graph | 话题图 |
| launch system | 启动系统 |
| rosbag playback | rosbag 回放 |
| robotics middleware | 机器人中间件 |

## 60-second Speaking Draft

This week I learned the basics of ROS2.

I built a small fake distance sensor system with a publisher and a subscriber.

The publisher sends `Range` messages to a topic, and the subscriber receives those messages.

I also learned how to start multiple nodes with a launch file and how to record topic data with rosbag.

Next week I plan to start learning basic computer vision and perception.

## 4. Git 收尾

```bash
git status
git add notes/week02 notes/glossary/robotics-terms.md
git commit -m "Add Week 2 ROS2 learning plans and review"
git push
```

## 完成标准

- [ ] `weekly-review-w02.md` 已填写
- [ ] glossary 已更新 Week 2 词汇
- [ ] Git 已 commit / push
- [ ] 明确 Week 3 下一步
