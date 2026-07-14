# Week 3 Day 04 - FPS and Latency Metrics

> 状态：**未开始**

## Today's Goal

- [ ] 理解 inference time / latency
- [ ] 理解 FPS
- [ ] 看懂 `detect_video.py` 的性能统计逻辑

## 1. 学（30 分钟）

重点阅读：

- `start = time.perf_counter()`
- `infer_ms = (time.perf_counter() - start) * 1000.0`
- `total_infer_ms += infer_ms`
- `avg_ms = total_infer_ms / frame_count`
- `FPS = 1000.0 / avg_ms`

回答：

- inference time 是什么？
- latency 是什么？
- FPS 是什么？
- 为什么 `1000.0 / avg_ms` 可以得到 FPS？
- robotics perception 为什么关心实时性？

## 2. 练（30 分钟）

运行：

```bash
cd week03_vision_demo
source .venv/bin/activate
python detect_video.py --source sample/sample.mp4 --max-frames 150
```

记录：

- Avg inference 是多少 ms？
- Avg FPS 是多少？
- 每 30 帧打印一次的统计怎么看？

可选：比较不同模型：

```bash
python detect_video.py --source sample/sample.mp4 --model yolov8n.pt --max-frames 100
python detect_video.py --source sample/sample.mp4 --model yolov8s.pt --max-frames 100
```

## 3. 记中文笔记（10 分钟）

- 模型越大，可能发生什么？
- FPS 越高代表什么？
- 如果机器人 perception 太慢，会有什么风险？

## 4. English Summary + Key Terms（10 分钟）

| English | 中文 |
|---------|------|
| FPS | 每秒帧数 |
| latency | 延迟 |
| inference time | 推理时间 |
| throughput | 吞吐量 |
| benchmark | 性能测试 |

## 60-second Speaking Draft

Today I learned how to measure FPS and latency in a vision demo.

Inference time means how long the model takes to process one frame.

FPS means how many frames can be processed per second.

These metrics are important because a robot needs timely perception to react safely.

## 完成标准

- [ ] 能解释 inference time
- [ ] 能解释 FPS
- [ ] 能记录一次运行的 Avg FPS
- [ ] 本日志已填写

## Git Commit

- Commit message：
- Pushed to GitHub：No
