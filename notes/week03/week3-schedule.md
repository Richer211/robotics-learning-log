# Week 3 日程表 — Vision Demo

Week 3 目标：从 ROS2 通信基础过渡到 **computer vision / perception**。本周不急着接 ROS2，先在普通 Python 项目里跑通 OpenCV + YOLO 视频检测，并理解 FPS / latency，为 Week 4 的 ROS2 vision pipeline 做准备。

| 天 | 主题 | 产出 | 日志 | 建议 Key Terms |
|----|------|------|------|----------------|
| Day 01 | Vision 环境 + demo 跑通 | `detect_video.py` 能跑 | `day01.md` | OpenCV, YOLO, virtual environment, dependency, model weights |
| Day 02 | OpenCV 视频读取 | 理解 `VideoCapture`、frame、writer | `day02.md` | frame, video capture, codec, resolution, video writer |
| Day 03 | YOLO 推理 | 理解 model / confidence / detection result | `day03.md` | inference, confidence, bounding box, detection, class label |
| Day 04 | FPS / latency 指标 | 看懂平均推理时间和 FPS | `day04.md` | FPS, latency, throughput, benchmark, performance |
| Day 05 | 小改需求 + 实验 | 改 `--conf` / `--max-frames` / output | `day05.md` | threshold, experiment, output video, parameter, validation |
| Day 06 | 连接 Week 4 | 画出 video → perception → ROS2 topic 的过渡图 | `day06.md` | image topic, perception pipeline, camera, cv_bridge, integration |
| Day 07 | 周复盘 | Week 3 review + Week 4 准备 | `weekly-review-w03.md` | review, milestone, portfolio, perception engineer, next steps |

## 每日英文（Week 3）

- **必做**：English Summary（3–5 句）+ Key Terms（5–10 个）→ 抄到 [`../glossary/robotics-terms.md`](../glossary/robotics-terms.md)
- **继续**：60-second Speaking Draft
- **新增**：每周 2 个 Interview Q&A，围绕 vision / perception

## Week 3 结束标准

- [ ] 能创建并使用 Python virtual environment
- [ ] `week03_vision_demo/detect_video.py` 能处理视频或 webcam
- [ ] 能解释 OpenCV 如何读取 frame
- [ ] 能解释 YOLO detection 的基本输出
- [ ] 能解释 confidence threshold 的作用
- [ ] 能看懂 FPS / latency 的含义
- [ ] 能说明 Week 3 standalone vision demo 如何在 Week 4 接入 ROS2 topic

## Week 3 学习原则

- 先跑通，再看代码，再改参数。
- 不追求模型训练，先理解 inference pipeline。
- 不急着学复杂深度学习数学，重点是工程流程：video input → model inference → annotated output → metrics。
