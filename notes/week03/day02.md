# Week 3 Day 02 - OpenCV Video Reading

> 状态：**未开始**

## Today's Goal

- [ ] 理解 OpenCV 如何读取视频
- [ ] 理解 frame、resolution、FPS、VideoWriter
- [ ] 读懂 `detect_video.py` 里视频输入/输出部分

## 1. 学（30 分钟）

重点阅读 `detect_video.py`：

- `open_capture(source)`
- `cv2.VideoCapture(...)`
- `cap.read()`
- `cv2.VideoWriter(...)`
- `writer.write(annotated)`

回答：

- `cv2.VideoCapture` 是什么？
- `cap.read()` 返回的 `ok, frame` 分别是什么意思？
- frame 可以理解成什么？
- `VideoWriter` 是干什么的？
- `width`、`height`、`fps_in` 从哪里来？

## 2. 练（30 分钟）

运行短视频测试：

```bash
cd week03_vision_demo
source .venv/bin/activate
python detect_video.py --source sample/sample.mp4 --max-frames 60
```

观察：

- 处理了多少帧？
- 输出视频是否生成？
- 输出视频尺寸是否和输入视频一致？

可选：用 webcam 测试：

```bash
python detect_video.py --source 0 --max-frames 60
```

## 3. 记中文笔记（10 分钟）

- 视频为什么可以被拆成一帧一帧？
- `frame` 和 Week 2 的 `Range message` 有什么相似点？
- output video 是怎么生成的？

## 4. English Summary + Key Terms（10 分钟）

| English | 中文 |
|---------|------|
| frame | 图像帧 |
| video capture | 视频读取 |
| resolution | 分辨率 |
| video writer | 视频写入器 |
| codec | 编解码器 |

## 60-second Speaking Draft

Today I learned how OpenCV reads video data.

A video can be processed frame by frame.

Each frame is an image, and the detection model runs on each image.

The annotated frames are written back into a new output video.

## 完成标准

- [ ] 能解释 `cv2.VideoCapture`
- [ ] 能解释 `cap.read()`
- [ ] 能解释 `VideoWriter`
- [ ] 本日志已填写

## Git Commit

- Commit message：
- Pushed to GitHub：No
