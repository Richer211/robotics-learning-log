# Week 3 Day 05 - Modify Vision Demo Requirement

> 状态：**未开始**

## Today's Goal

- [ ] 对 `detect_video.py` 做一个小改动或参数实验
- [ ] 对比修改前后的输出
- [ ] 理解参数变化如何影响 detection behavior

## 1. 学（20 分钟）

回顾：

- `--conf`
- `--max-frames`
- `--output`
- `--model`

回答：

- `--conf` 调高会发生什么？
- `--max-frames` 对调试有什么帮助？
- 为什么 output video 不提交到 Git？
- 如果换模型，速度和检测效果可能怎么变化？

## 2. 练（40 分钟）

任选一个实验：

1. 比较 `--conf 0.3`、`--conf 0.5`、`--conf 0.7`
2. 修改默认 output 文件名
3. 增加每 10 帧打印一次统计，而不是每 30 帧
4. 只跑 `--max-frames 30` 做快速验证

推荐先做参数实验：

```bash
cd week03_vision_demo
source .venv/bin/activate
python detect_video.py --source sample/sample.mp4 --conf 0.3 --max-frames 100
python detect_video.py --source sample/sample.mp4 --conf 0.7 --max-frames 100
```

## 3. 记中文笔记（10 分钟）

- 今天改了什么？
- 运行结果有什么变化？
- 哪个参数最适合快速调试？
- 这个实验和真实机器人 perception 有什么关系？

## 4. English Summary + Key Terms（10 分钟）

| English | 中文 |
|---------|------|
| parameter | 参数 |
| experiment | 实验 |
| validation | 验证 |
| output video | 输出视频 |
| detection behavior | 检测行为 |

## 60-second Speaking Draft

Today I changed a parameter in the vision demo and compared the result.

I learned that a confidence threshold can change how many detections are shown.

Small experiments like this help me understand the behavior of a perception system.

This is similar to tuning parameters in a real robotics pipeline.

## Interview Practice

**Q: Why do perception engineers tune confidence thresholds?**

A: They tune confidence thresholds to balance false positives and false negatives, depending on the application and safety requirements.

## 完成标准

- [ ] 完成一个参数实验或小代码改动
- [ ] 记录修改前后差异
- [ ] 能解释这个参数的作用
- [ ] 本日志已填写

## Git Commit

- Commit message：
- Pushed to GitHub：No
