# Week 3: Vision Demo

Video object detection with OpenCV + Ultralytics YOLO, with FPS / latency stats.

Runs on **macOS or Ubuntu** (GPU optional).

## Setup

```bash
cd week03_vision_demo
python3 -m venv .venv # 创建项目专属 Python 环境
source .venv/bin/activate   # 启用这个环境
pip install -r requirements.txt # 安装项目依赖
```

First run downloads YOLO weights (e.g. `yolov8n.pt`).

## Run

```bash
# Video file
python detect_video.py --source sample/sample.mp4

# Webcam
python detect_video.py --source 0

# Limit frames for quick test
python detect_video.py --source sample/sample.mp4 --max-frames 100
```

## Output

- Annotated video: `output/annotated.mp4` (gitignored)
- Console: per-30-frame and final average inference time / FPS

## Example

```text
Frame 30: infer=42.3 ms, avg=45.1 ms, FPS=22.2
--- Summary ---
Frames: 150
Avg inference: 44.80 ms
Avg FPS: 22.32
Output: week03_vision_demo/output/annotated.mp4
```

## Notes

- Use a short clip for learning; full movies are slow and unnecessary.
- This demo is standalone — Week 4 integrates detection into ROS2 topics.
