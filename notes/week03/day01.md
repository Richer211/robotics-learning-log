# Week 3 Day 01 - Vision Environment and First Detection Run

> 状态：**已完成** — 虚拟环境、依赖安装、YOLO 检测跑通，并生成 annotated output video。

## Today's Goal

- [x] 创建 Python virtual environment
- [x] 安装 OpenCV / Ultralytics / NumPy
- [x] 跑通 `week03_vision_demo/detect_video.py`
- [x] 理解 Week 3 demo 和 Week 4 ROS2 vision 的关系

## 1. 学（30 分钟）

阅读：

- [`../../week03_vision_demo/README.md`](../../week03_vision_demo/README.md)
- `week03_vision_demo/detect_video.py` 的参数部分

回答：

### Week 3 vision demo 做什么？

Week 3 vision demo 用 OpenCV 读取视频，再用 YOLOv8 对每一帧做目标检测，最后输出：

1. 带检测框的 annotated video
2. 终端里的 inference time / FPS 统计

最小流程是：

```text
video file
→ OpenCV 读取 frame
→ YOLO 推理
→ 画 bounding box
→ 输出 annotated video + FPS / latency
```

### 为什么这周可以先在 macOS 上跑，而不是必须在 Ubuntu VM 里跑？

因为 Week 3 先学的是 standalone Python vision pipeline，还没有接入 ROS2 Humble。

OpenCV、Ultralytics YOLO、NumPy 都可以在 macOS 的 Python 虚拟环境里运行。

Week 4 才会把类似的 vision 流程接到 ROS2 topic 上，那时再回到 Ubuntu VM。

### `requirements.txt` 是干什么的？

`requirements.txt` 列出这个项目需要的 Python 依赖包。

本项目里包括：

```text
opencv-python
ultralytics
numpy
```

用下面这条命令，可以一次把依赖安装到当前虚拟环境：

```bash
pip install -r requirements.txt
```

### `yolov8n.pt` 是什么？

`yolov8n.pt` 是已经训练好的 YOLOv8 预训练权重文件。

- `yolov8`：模型系列
- `n`：nano，表示轻量级版本，适合快速实验
- `.pt`：PyTorch 权重文件

第一次运行时，程序会自动下载这个文件。它是通用目标检测模型，主要识别人、车、杯子等常见物体，不一定专门适合机器人运动轨迹视频。

## 2. 练（30 分钟）

在 macOS 里执行：

```bash
cd week03_vision_demo
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

我实际放的视频是：

```text
week03_vision_demo/sample/robotic_routine.MP4
```

运行：

```bash
python detect_video.py --source sample/robotic_routine.MP4
```

也做过参数实验：

```bash
python detect_video.py --source sample/robotic_routine.MP4 --conf 0.25 --max-frames 200
```

说明：

- `--source`：输入视频路径
- `--conf`：confidence threshold，只有置信度高于这个值的检测结果才会保留
- `--max-frames 200`：最多处理 200 帧，方便快速测试

## 3. 记中文笔记（10 分钟）

### 环境是否安装成功？

成功。`.venv` 已创建，`pip install -r requirements.txt` 已安装 OpenCV、Ultralytics、NumPy 等依赖。

### 第一次运行是否下载 YOLO weights？

是的，第一次运行时自动下载了 `yolov8n.pt`。

### 输出视频生成在哪里？

```text
week03_vision_demo/output/annotated.mp4
```

这个视频里已经有 YOLO 画出来的检测框。

### 终端有没有打印 FPS / inference time？

有。示例输出：

```text
Running detection: source=sample/robotic_routine.MP4, model=yolov8n.pt
Frame 30: infer=43.1 ms, avg=82.7 ms, FPS=12.1
Frame 60: infer=41.7 ms, avg=64.7 ms, FPS=15.5
Frame 90: infer=45.8 ms, avg=58.9 ms, FPS=17.0
```

含义：

- `Frame 30`：已处理 30 帧
- `infer=43.1 ms`：这一帧推理用了 43.1 毫秒
- `avg=82.7 ms`：目前平均每帧推理时间
- `FPS=12.1`：平均每秒大约处理 12.1 帧

刚开始平均 FPS 较低，是因为模型加载和系统预热；后面会逐渐稳定。

### 有无报错？如何解决？

没有严重报错。

中间遇到过路径空格问题：

```text
zsh: no such file or directory: /Users/ganggang/Documents/Robotics
```

原因是路径 `Robotics Learning` 中间有空格，shell 把它截断了。正确做法是给完整路径加引号，或者直接在已激活的 `.venv` 里使用：

```bash
python detect_video.py --source sample/robotic_routine.MP4
```

### 检测框为什么不稳定？

输出视频里有检测框，但不是每一帧都持续框住目标。原因包括：

1. `yolov8n.pt` 是通用模型，不一定专门适合机器人运动轨迹视频。
2. 当前脚本是逐帧 detection，没有 tracking，所以下一帧 confidence 不够时框会消失。
3. 默认 `--conf 0.4` 会过滤掉低置信度结果。

这不代表 demo 失败，只说明 perception pipeline 已经跑通，但检测效果还取决于模型和参数。

## 4. English Summary + Key Terms（10 分钟）

## English Summary

Today I set up the Week 3 vision demo on macOS.

I created a Python virtual environment and installed OpenCV, Ultralytics, and NumPy.

Then I ran YOLO object detection on a robot motion video and generated an annotated output video.

I also learned that FPS and inference time help measure how fast the perception pipeline can process each frame.

The detection boxes were not always stable, because the model is a general pretrained model and the script detects each frame independently.

| English | 中文 |
|---------|------|
| OpenCV | 计算机视觉库 |
| YOLO | 实时目标检测模型 |
| virtual environment | Python 虚拟环境 |
| dependency | 依赖 |
| model weights | 模型权重 |
| inference | 推理 |
| FPS | 每秒帧数 |
| annotated video | 标注后视频 |
| confidence threshold | 置信度阈值 |
| bounding box | 检测框 |

## 60-second Speaking Draft

Today I started the Week 3 vision demo.

I created a Python virtual environment and installed the required dependencies.

Then I ran a YOLO object detection script on a robot motion video.

The program generated an annotated output video and printed FPS and inference time.

This demo helps me understand the basic perception pipeline before connecting vision to ROS2 in Week 4.

## 完成标准

- [x] `.venv` 创建成功
- [x] `pip install -r requirements.txt` 成功
- [x] `detect_video.py` 至少跑通一次
- [x] 本日志已填写

## Git Commit

- Commit message： learn week03/day01.md
- Pushed to GitHub：Yes
