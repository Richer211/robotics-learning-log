# Week 3 Day 03 - YOLO Inference and Detection Results

> 状态：**已完成** — 跑通了不同 confidence threshold 下的检测框数量对比，理解了 inference 输出结构和 `.plot()` 的作用。

## Today's Goal

- [x] 理解 YOLO inference 的基本流程
- [x] 理解 confidence threshold
- [x] 理解 detection result / bounding box / class label

## 1. 学（30 分钟）

重点阅读 `detect_video.py`：

- `from ultralytics import YOLO`
- `model = YOLO(args.model)`
- `results = model.predict(frame, conf=args.conf, verbose=False)`
- `annotated = results[0].plot()`

回答：

### `YOLO(args.model)` 是干什么的？

用来加载 `yolov8n.pt` 这个预训练模型权重文件，创建一个可以直接拿来做推理的模型对象。

### `model.predict(...)` 输入和输出分别是什么？

- 输入：`frame`（一帧图像）、`conf`（置信度阈值）、`verbose`（是否打印详细日志）。
- 输出：一个**列表**，列表里每个元素是一个 `Results` 对象——对应输入的每一张图像的检测结果（这里因为只传了一帧，所以列表长度永远是 1，即 `results[0]`）。`Results` 对象内部包含 `boxes`（检测框信息）、`orig_img`（原始图像）等属性，不是"Detection 对象"。



### `conf=args.conf` 控制什么？

控制过滤阈值。模型对每个候选检测框都会给出一个置信度分数，只有分数 **≥ conf** 的框才会被保留下来显示；`conf` 越低，保留的框越多，`conf` 越高，保留的框越少。

### `results[0].plot()` 做了什么？

它是针对**这一帧图像**的操作：把 `results[0]` 里的检测框、类别标签、置信度分数画在这一帧原始图像的副本上，返回一张**带标注的图像**（不是视频）。视频是靠 `writer.write(annotated)` 把这些标注后的图像逐帧写入 `VideoWriter`，一帧一帧攒出来的。

### bounding box 和 class label 分别是什么？

- bounding box（检测框）：模型认为物体所在位置的矩形框坐标。
- class label（类别标签）：模型认为这个框里是什么物体，比如 `person`、`car`。



## 2. 练（30 分钟）

运行默认 confidence（实际用的是自己放的机器人视频 `robotic_routine.MP4`，不是不存在的 `sample.mp4`）：

```bash
cd week03_vision_demo
source .venv/bin/activate
python detect_video.py --source sample/robotic_routine.MP4 --conf 0.4 --max-frames 100
```

```text
--- Summary ---
Frames: 100
Avg inference: 48.33 ms
Avg FPS: 20.69
Output: week03_vision_demo/output/annotated.mp4
```

再运行较高 confidence：

```bash
python detect_video.py --source sample/robotic_routine.MP4 --conf 0.7 --max-frames 100
```

又追加测试了一个更低的 confidence，验证阈值和检测框数量的关系：

```bash
python detect_video.py --source sample/robotic_routine.MP4 --conf 0.1 --max-frames 100
```

三组结果对比（100 帧内检测框总数）：


| conf | 检测框总数（100 帧内） | 说明                     |
| ---- | ------------- | ---------------------- |
| 0.7  | 0             | 每一帧都是 0                |
| 0.4  | 1             | 只有第 85 帧检测到 1 个        |
| 0.1  | 数十个           | 从第 82 帧开始密集出现，最多单帧 4 个 |


观察：

### `0.4` 和 `0.7` 哪个检测框更多？

`0.4` 更多：`0.4` 检测出 1 个，`0.7` 是 0 个。这符合"阈值越低，保留框越多"的规律（0.4 的结果应该是 0.7 结果的超集）。

### confidence threshold 变高后，误检可能减少还是增加？

误检可能会减少，因为只有置信度更高的框才会被保留，一些"模糊、不确定"的候选框会被过滤掉。但同时也会有**漏检增加**的代价——真实存在但置信度不够高的物体也会被一起过滤掉。

### 额外发现：`conf=0.1` 时检测框数量明显变多，说明了什么？

说明这段视频前半段画面里，模型给出的候选框置信度普遍低于 0.4，只有降到 0.1 才能"捞"出来。同时也观察到检测结果有明显的**聚集现象**——前 30 帧几乎全是 0，第 82 帧之后才密集出现检测框，可能是视频后半段物体角度/距离变得更容易被模型识别。但 `conf=0.1` 这么低的阈值也意味着**误检风险变高**，需要拉出标注视频人工确认这些框是不是真的框住了合理的物体。

## 3. 记中文笔记（10 分钟）



### YOLO 是在检测什么？

检测每一帧图像里出现的物体，输出它们的位置（bounding box）和类别（class label）。

### confidence threshold 越高代表什么？

代表模型对自己的判断要求更严格——只有分数足够高的检测框才会被保留下来，所以检测框数量通常会变少。

### 为什么 robotics perception 需要关心误检和漏检？

因为误检（false positive，把不存在的物体当成存在）和漏检（false negative，真实存在的物体没检测到）都会导致感知数据不准确，进而影响机器人后续的决策（比如避障、抓取），在真实环境里可能导致任务失败甚至安全问题。

## 4. English Summary + Key Terms（10 分钟）



## English Summary

Today I learned how YOLO inference works on a single video frame.

`model.predict()` returns a list of `Results` objects, one per input image, and each `Results` object contains the detected bounding boxes and class labels.

I learned that `results[0].plot()` draws the detections onto one frame and returns an annotated image, not a video — the output video is built frame by frame using `VideoWriter`.

I also tested how the confidence threshold affects the number of detections: a lower threshold (0.1) kept far more boxes than a higher threshold (0.7), which confirmed that a lower threshold reduces false negatives but increases the risk of false positives.


| English        | 中文     |
| -------------- | ------ |
| inference      | 推理     |
| confidence     | 置信度    |
| bounding box   | 检测框    |
| class label    | 类别标签   |
| false positive | 误检     |
| false negative | 漏检     |
| Results object | 检测结果对象 |




## 60-second Speaking Draft

Today I learned how the YOLO model performs object detection.

The model takes one video frame as input and returns detection results.

Each result can include a bounding box, a class label, and a confidence score.

Changing the confidence threshold can change how many detections are shown — a lower threshold detects more objects but may include more false positives.

## Interview Practice

**Q: What is object detection?**

A: Object detection is a computer vision task that finds objects in an image and predicts their bounding boxes and class labels.

**Q: What happens if you lower the confidence threshold?**

A: Lowering the confidence threshold keeps more detection boxes, which can reduce false negatives (missed objects) but increases the risk of false positives (incorrect detections).

## 完成标准

- [x] 能解释 YOLO inference
- [x] 能解释 confidence threshold
- [x] 能比较 `--conf 0.4` 和 `--conf 0.7`
- [x] 本日志已填写



## Git Commit

- Commit message：learn yolo and conf defintion
- Pushed to GitHub：Yes

