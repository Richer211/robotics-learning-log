# Week 3 Day 02 - OpenCV Video Reading

> 状态：**已完成** — 已跑通 `detect_video.py` 的视频读取/写入流程，并理解 frame、VideoCapture、VideoWriter。

## Today's Goal

- [x] 理解 OpenCV 如何读取视频
- [x] 理解 frame、resolution、FPS、VideoWriter
- [x] 读懂 `detect_video.py` 里视频输入/输出部分

## 1. 学（30 分钟）

重点阅读 `detect_video.py`：

- `open_capture(source)`
- `cv2.VideoCapture(...)`
- `cap.read()`
- `cv2.VideoWriter(...)`
- `writer.write(annotated)`

回答：

### `cv2.VideoCapture` 是什么？

`cv2.VideoCapture` 是 OpenCV 提供的视频读取对象，负责打开视频文件（或摄像头），并解码出一张一张的图像帧供程序使用。

本项目里的 `open_capture(source)` 会根据 `source` 是数字（摄像头编号）还是路径（视频文件），分别调用：

```python
cv2.VideoCapture(int(source))   # webcam
cv2.VideoCapture(str(source))   # 视频文件
```

### `cap.read()` 返回的 `ok, frame` 分别是什么意思？

- `ok`：布尔值，表示这一次是否成功读取到一帧。视频读完或摄像头断开时会变成 `False`。
- `frame`：读取到的这一帧图像数据，是一个 NumPy 数组（高度 × 宽度 × 通道）。

代码里用它来判断是否结束：

```python
ok, frame = cap.read()
if not ok:
  break
```

### frame 可以理解成什么？

frame 就是组成视频的其中一张静止图像。视频本质上是很多张 frame 按固定速率连续播放形成的动态画面。

### `VideoWriter` 是干什么的？

`VideoWriter` 负责把处理后的图像**逐帧写入**一个新的视频文件，而不是一次性生成整个视频。

程序每处理完一帧（YOLO 推理 + 画检测框）就调用一次：

```python
writer.write(annotated)
```

所有帧写完之后，`output` 才是一个完整的、可以播放的视频。

### `width`、`height`、`fps_in` 从哪里来？

```python
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps_in = cap.get(cv2.CAP_PROP_FPS) or 30.0
```

它们都是从 `cap = open_capture(args.source)` 这个输入视频对象里读出来的，也就是**直接取自输入视频本身的分辨率和帧率**。`VideoWriter` 用这组参数创建输出视频，所以理论上输出视频尺寸和输入视频应该一致。

## 2. 练（30 分钟）

运行短视频测试：

```bash
cd week03_vision_demo
source .venv/bin/activate
python detect_video.py --source sample/robotic_routine.MP4 --max-frames 60
```

实际输出：

```text
Running detection: source=sample/robotic_routine.MP4, model=yolov8n.pt
Frame 30: infer=40.3 ms, avg=71.8 ms, FPS=13.9
Frame 60: infer=41.0 ms, avg=57.5 ms, FPS=17.4
--- Summary ---
Frames: 60
Avg inference: 57.49 ms
Avg FPS: 17.39
Output: week03_vision_demo/output/annotated.mp4
```

观察：

- 处理了多少帧？60 帧（因为设置了 `--max-frames 60`）。
- 输出视频是否生成？生成了，路径是 `week03_vision_demo/output/annotated.mp4`。
- 输出视频尺寸是否和输入视频一致？应该一致，因为 `width`/`height` 直接来自输入视频的 `cap.get(...)`。可以用 Finder「显示简介」或 `ffprobe output/annotated.mp4` 查看分辨率，和原视频对比确认。

可选：用 webcam 测试：

```bash
python detect_video.py --source 0 --max-frames 60
```

## 3. 记中文笔记（10 分钟）

### 视频为什么可以被拆成一帧一帧？

视频本身就是由一张一张静止图像（frame）按固定速率（FPS）连续存储和播放组成的。比如 30 FPS 的视频，每秒钟就有 30 张独立图像。

`cv2.VideoCapture` 负责打开并解码视频文件，`cap.read()` 每调用一次就取出下一张图像。

注意：代码里的 `if frame_count % 30 == 0` 只是「每处理 30 帧打印一次统计信息」，和「视频为什么能拆成帧」没有关系——不是「30 张图片算一帧」，是每处理完 30 帧就输出一次进度。

### `frame` 和 Week 2 的 `Range message` 有什么相似点？

两者都是**随时间连续产生的离散数据样本**：

- `Range message`：距离传感器每隔固定时间（0.5 秒）发布一次距离读数。
- `frame`：摄像头每隔固定时间（1/FPS 秒）产生一张图像。

下游程序处理方式也类似：subscriber 的 `callback` 每收到一条 message 处理一次；这里的检测循环每读到一个 frame 就调用一次 YOLO 推理。两者都是「持续产生数据 → 逐个处理」的模式。

### output video 是怎么生成的？

先用 YOLO 对每一帧做推理：

```python
results = model.predict(frame, conf=args.conf, verbose=False)
annotated = results[0].plot()
```

`results[0].plot()` 把检测框画在原始 frame 上，生成 `annotated` 图像。再用 `VideoWriter` 把这个 `annotated` 帧写进输出视频：

```python
writer.write(annotated)
```

所以输出视频里看到的画面，是「原始画面 + YOLO 检测框」，不是原始视频本身。

## 4. English Summary + Key Terms（10 分钟）

## English Summary

Today I learned how OpenCV reads and writes video data.

`cv2.VideoCapture` opens a video file and decodes it frame by frame, while `cap.read()` returns whether a frame was read and the frame itself.

I learned that `VideoWriter` writes one annotated frame at a time, not the whole video at once.

I also learned that the output video's width, height, and FPS come directly from the input video, so both should have the same resolution.

| English | 中文 |
|---------|------|
| frame | 图像帧 |
| video capture | 视频读取 |
| resolution | 分辨率 |
| video writer | 视频写入器 |
| codec | 编解码器 |
| decode | 解码 |
| frame rate | 帧率 |

## 60-second Speaking Draft

Today I learned how OpenCV reads video data.

A video can be processed frame by frame.

Each frame is an image, and the detection model runs on each image.

The annotated frames are written back into a new output video, one frame at a time.

## 完成标准

- [x] 能解释 `cv2.VideoCapture`
- [x] 能解释 `cap.read()`
- [x] 能解释 `VideoWriter`
- [x] 本日志已填写

## Git Commit

- Commit message：
- Pushed to GitHub：No
