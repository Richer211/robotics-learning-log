# Week 3 Day 03 - YOLO Inference and Detection Results

> 状态：**未开始**

## Today's Goal

- [ ] 理解 YOLO inference 的基本流程
- [ ] 理解 confidence threshold
- [ ] 理解 detection result / bounding box / class label

## 1. 学（30 分钟）

重点阅读 `detect_video.py`：

- `from ultralytics import YOLO`
- `model = YOLO(args.model)`
- `results = model.predict(frame, conf=args.conf, verbose=False)`
- `annotated = results[0].plot()`

回答：

- `YOLO(args.model)` 是干什么的？
- `model.predict(...)` 输入和输出分别是什么？
- `conf=args.conf` 控制什么？
- `results[0].plot()` 做了什么？
- bounding box 和 class label 分别是什么？

## 2. 练（30 分钟）

运行默认 confidence：

```bash
cd week03_vision_demo
source .venv/bin/activate
python detect_video.py --source sample/sample.mp4 --conf 0.4 --max-frames 100
```

再运行较高 confidence：

```bash
python detect_video.py --source sample/sample.mp4 --conf 0.7 --max-frames 100
```

观察：

- `0.4` 和 `0.7` 哪个检测框更多？
- confidence threshold 变高后，误检可能减少还是增加？

## 3. 记中文笔记（10 分钟）

- YOLO 是在检测什么？
- confidence threshold 越高代表什么？
- 为什么 robotics perception 需要关心误检和漏检？

## 4. English Summary + Key Terms（10 分钟）

| English | 中文 |
|---------|------|
| inference | 推理 |
| confidence | 置信度 |
| bounding box | 检测框 |
| class label | 类别标签 |
| false positive | 误检 |
| false negative | 漏检 |

## 60-second Speaking Draft

Today I learned how the YOLO model performs object detection.

The model takes one video frame as input and returns detection results.

Each result can include a bounding box, a class label, and a confidence score.

Changing the confidence threshold can change how many detections are shown.

## Interview Practice

**Q: What is object detection?**

A: Object detection is a computer vision task that finds objects in an image and predicts their bounding boxes and class labels.

## 完成标准

- [ ] 能解释 YOLO inference
- [ ] 能解释 confidence threshold
- [ ] 能比较 `--conf 0.4` 和 `--conf 0.7`
- [ ] 本日志已填写

## Git Commit

- Commit message：
- Pushed to GitHub：No
