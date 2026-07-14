# Week 3 Day 06 - Connect Vision Demo to Week 4 ROS2 Vision

> 状态：**未开始**

## Today's Goal

- [ ] 理解 Week 3 standalone vision demo 和 Week 4 ROS2 vision 的关系
- [ ] 画出 video → detection → metrics → ROS2 topic 的概念图
- [ ] 阅读 Week 4 README 的 architecture 部分

## 1. 学（30 分钟）

阅读：

- [`../../week04_ros2_vision/README.md`](../../week04_ros2_vision/README.md)
- Week 3 `detect_video.py`

回答：

- Week 3 是 standalone demo，Week 4 会多出什么？
- `/camera/image_raw` 是什么？
- `/perception/detections` 可能发送什么？
- `/perception/metrics` 可能发送什么？
- `cv_bridge` 大概解决什么问题？

## 2. 练（30 分钟）

画出最小概念图：

```text
Week 3:
video file -> OpenCV frame -> YOLO -> annotated video + FPS

Week 4:
video file -> ROS2 /camera/image_raw -> perception_node -> detections + metrics topics
```

在本文件里写一段自己的理解：

```text
Week 3 先学习普通 Python 视觉流程；
Week 4 把这个视觉流程放进 ROS2 node 和 topic 里。
```

## 3. 记中文笔记（10 分钟）

- 为什么 Week 3 不直接上 ROS2？
- Week 4 接 ROS2 后，多了哪些工程概念？
- camera frame 和 Week 2 的 Range message 有什么相似点？

## 4. English Summary + Key Terms（10 分钟）

| English | 中文 |
|---------|------|
| image topic | 图像话题 |
| perception pipeline | 感知流程 |
| camera frame | 相机帧 |
| cv_bridge | ROS 图像和 OpenCV 转换工具 |
| integration | 集成 |

## 60-second Speaking Draft

Today I connected the Week 3 vision demo to the Week 4 ROS2 vision plan.

Week 3 focuses on a standalone Python perception pipeline.

Week 4 will wrap similar vision logic inside ROS2 nodes and topics.

This helps me understand how computer vision becomes part of a robotics system.

## 完成标准

- [ ] 能解释 Week 3 和 Week 4 的区别
- [ ] 能画出最小 vision pipeline
- [ ] 能解释 image topic 的基本概念
- [ ] 本日志已填写

## Git Commit

- Commit message：
- Pushed to GitHub：No
