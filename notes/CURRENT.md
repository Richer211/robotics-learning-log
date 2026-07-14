# 当前学习进度（每天只看这个文件）

> 更新规则：每完成一天，把「今天做」改成下一天的内容。

## 你现在的位置

- **阶段**：Month 1 / Week 3
- **已完成**：Week 1 基础工程 + Week 2 ROS2 Basics
- **今天**：Week 3 Day 01 — Vision 环境 + 第一次 YOLO detection run
- **本周目标**：跑通 OpenCV + YOLO 视频检测，理解 frame、inference、FPS / latency，为 Week 4 ROS2 vision integration 做准备

## 今天做这 5 件事（Week 3 Day 01）

### 1. 学（30 分钟）

阅读：

- [`notes/week03/week3-schedule.md`](week03/week3-schedule.md)
- [`notes/week03/day01.md`](week03/day01.md)
- [`week03_vision_demo/README.md`](../week03_vision_demo/README.md)
- `week03_vision_demo/detect_video.py` 的参数部分

重点回答：

- Week 3 vision demo 做什么？
- 为什么这周可以先在 macOS 上跑，而不是必须在 Ubuntu VM 里跑？
- `requirements.txt` 是干什么的？
- `yolov8n.pt` 是什么？

### 2. 练（30 分钟）

在 macOS 里创建 Python virtual environment：

```bash
cd "/Users/ganggang/Documents/Robotics Learning/week03_vision_demo"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

准备一个短视频，放到：

```text
week03_vision_demo/sample/sample.mp4
```

运行：

```bash
python detect_video.py --source sample/sample.mp4 --max-frames 100
```

也可以用 webcam：

```bash
python detect_video.py --source 0 --max-frames 100
```

### 3. 记中文笔记（10 分钟）

填写 [`notes/week03/day01.md`](week03/day01.md)：

- 环境是否安装成功？
- 第一次运行是否下载 YOLO weights？
- 输出视频生成在哪里？
- 终端有没有打印 FPS / inference time？
- 有无报错？如何解决？

### 4. 写英文输出（10 分钟）

在 [`notes/week03/day01.md`](week03/day01.md) 填写：

1. **English Summary**（3–5 句）
2. **Key Terms**（5–10 个）
3. **60-second Speaking Draft**

新词同步到 [`notes/glossary/robotics-terms.md`](glossary/robotics-terms.md)。

### 5. 提交（5 分钟）

```bash
cd "/Users/ganggang/Documents/Robotics Learning"
git status
git add notes/week03 notes/CURRENT.md notes/glossary/robotics-terms.md
git commit -m "Add Week 3 vision learning plan"
git push
```

> Git commit 一律用英文。

## 今天完成标准

- [ ] `.venv` 创建成功
- [ ] `pip install -r requirements.txt` 成功
- [ ] `detect_video.py` 至少跑通一次
- [ ] `notes/week03/day01.md` 已填写
- [ ] Day 01 English Summary + Key Terms 已填写
- [ ] 今天有英文 Git commit

## 英文学习分阶段（不用一次做完）

| 阶段 | 每天英文任务 |
|------|----------------|
| **Week 1（Day 02–07）** | English Summary + Key Terms（+10 min） |
| **Week 2 起** | 加上 60-second Speaking Draft（可先读稿） |
| **Week 3 起** | 每周 2 次 Interview Q&A（围绕 vision / perception） |
| **Month 2 起** | 录音 + 复盘，见 [`notes/speaking/README.md`](speaking/README.md) |

原则：**中文理解技术，英文沉淀表达；技术是主线，英文每天 +10 分钟。**

## 明天（Week 3 Day 02 预告）

- 理解 OpenCV 如何读取视频
- 学 `cv2.VideoCapture`、`cap.read()`、`VideoWriter`
- 把 video 理解成一帧一帧的 image stream
- 填写 [`notes/week03/day02.md`](week03/day02.md)

## 本周完整日程

见 [`notes/week03/week3-schedule.md`](week03/week3-schedule.md)（含每日建议 Key Terms）

## 每天固定节奏

```
看一点(30min) → 练一点(30min) → 记中文笔记(10min) → 写英文输出(10min) → git commit(5min)
```

## 学不好时问自己

1. 我今天写代码 / 敲命令了吗？
2. 我运行并看到结果了吗？
3. 我改过一个地方吗？
4. 我记下来了吗（中文 + 英文）？

四个都是 Yes，才算有效的一天。
