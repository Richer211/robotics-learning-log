# Week 3 Day 07 - Review and Prepare for Week 4

> 状态：**未开始**

## Today's Goal

- [ ] 完成 Week 3 复盘
- [ ] 整理 vision / perception 核心概念
- [ ] 更新 glossary
- [ ] 准备 Week 4 ROS2 + Vision integration

## 1. 回顾（30 分钟）

检查 Week 3 是否完成：

- [ ] Python virtual environment 可用
- [ ] OpenCV / Ultralytics / NumPy 安装成功
- [ ] `detect_video.py` 能处理 video 或 webcam
- [ ] 能解释 frame / VideoCapture / VideoWriter
- [ ] 能解释 YOLO inference / confidence / detection result
- [ ] 能解释 FPS / latency
- [ ] 能说明 Week 3 如何过渡到 Week 4 ROS2 vision

## 2. 复盘问题（30 分钟）

写在 [`weekly-review-w03.md`](weekly-review-w03.md)：

- Week 3 最重要的 3 个收获是什么？
- OpenCV 在 demo 中负责什么？
- YOLO 在 demo 中负责什么？
- FPS / latency 为什么重要？
- Week 4 把 vision 接入 ROS2 后，会多出哪些概念？
- 还有哪些概念不清楚？

## 3. English Summary + Key Terms（10 分钟）

整理 Week 3 Key Terms，并同步到 [`../glossary/robotics-terms.md`](../glossary/robotics-terms.md)：

| English | 中文 |
|---------|------|
| computer vision | 计算机视觉 |
| object detection | 目标检测 |
| inference pipeline | 推理流程 |
| annotated video | 标注后视频 |
| performance metrics | 性能指标 |
| perception engineer | 感知工程师 |

## 60-second Speaking Draft

This week I learned the basics of computer vision for robotics.

I ran a YOLO object detection demo on video data.

I learned how OpenCV reads video frames and how YOLO detects objects in each frame.

I also measured FPS and inference latency.

Next week I plan to connect this vision pipeline to ROS2 topics.

## 4. Git 收尾

```bash
git status
git add notes/week03 notes/glossary/robotics-terms.md
git commit -m "Add Week 3 vision learning plans"
git push
```

## 完成标准

- [ ] `weekly-review-w03.md` 已填写
- [ ] glossary 已更新 Week 3 词汇
- [ ] Git 已 commit / push
- [ ] 明确 Week 4 下一步
