# Weekly Review - Week 3

> 主题：Vision Demo

## 1. What I Built

- [ ] Python virtual environment
- [ ] OpenCV + YOLO detection demo
- [ ] Annotated output video
- [ ] FPS / latency metrics
- [ ] Week 3 → Week 4 vision pipeline concept map

## 2. What I Learned（中文）

### Vision / Perception 基础概念

写下你对以下概念的理解：

- computer vision：
- perception：
- OpenCV：
- YOLO：
- frame：
- inference：
- confidence threshold：
- FPS：
- latency：

### 本周最重要的 3 个收获

1.
2.
3.

## 3. Problems I Met

- 问题 1：
- 问题 2：
- 问题 3：

## 4. How I Solved Them

- 解决方式 1：
- 解决方式 2：
- 解决方式 3：

## 5. English Summary

This week I learned the basics of computer vision for robotics.

I ran a YOLO object detection demo on video data.

I learned how OpenCV reads video frames and how the model detects objects in each frame.

I also measured FPS and inference latency to understand basic perception performance.

## 6. Key Terms

| English | 中文 | Note |
|---------|------|------|
| computer vision | 计算机视觉 | Understanding images and videos with software |
| perception | 感知 | Interpreting sensor data to understand the environment |
| OpenCV | 计算机视觉库 | Used for video/image processing |
| YOLO | 实时目标检测模型 | Detects objects in images or video frames |
| frame | 图像帧 | One image from a video stream |
| inference | 推理 | Running a model to get predictions |
| confidence threshold | 置信度阈值 | Minimum confidence required to keep a detection |
| FPS | 每秒帧数 | Frames processed per second |
| latency | 延迟 | Time needed to process one frame |

## 7. 60-second Speaking Draft

This week I worked on a computer vision demo for robotics.

I used OpenCV to read video frames and YOLO to detect objects.

The script generates an annotated output video and prints FPS and latency statistics.

This helped me understand a basic perception pipeline.

Next week, I will connect a similar vision pipeline to ROS2 topics.

## 8. Interview Practice

**Q: What is the difference between computer vision and robotics perception?**

A: Computer vision focuses on understanding images and videos. Robotics perception uses vision and other sensor data to help a robot understand its environment and make decisions.

**Q: Why are FPS and latency important in robotics perception?**

A: They are important because a robot needs timely perception to react safely. If perception is too slow, the robot may respond too late.

## 9. Next Week Plan

- [ ] Start Week 4 ROS2 + vision integration
- [ ] Understand `/camera/image_raw`
- [ ] Learn how OpenCV frames become ROS2 image messages
- [ ] Continue English Summary and Interview Q&A
