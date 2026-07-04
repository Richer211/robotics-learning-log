# Day 03 - Robotics Learning

> 状态：**已完成** — Day 02 完成后再做。

## Today's Goal

- [x] 运行升级版 Python 假传感器
- [x] 理解 `FakeSensor` class 的每个方法
- [x] 自己改需求：告警距离 1.0m → 0.8m

## 运行命令

```bash
cd python_practice
python3 sensor_sim.py --frames 10 --interval 0.5
cat sensor_log.txt
```

## What I Finished

- [x] 运行 `sensor_sim.py` 并理解 `FakeSensor` 各方法
- [x] 将告警距离从 1.0m 改为 0.8m 并对比结果

## What I Learned

- class FakeSensor()表示创建一个传感器，内置了距离，温度以及是否发出警告
- def __init__: 先初始化参数
- def read_distance(self): 传感器可以感应到距离
- def def read_temperature(self):传感器的温度
- def is_warning: 传感器距离物体在WARNING_DISTANCE_M = 1时是否发出警告
- def format_reading: 将传感器的内置信息格式化返回
- def main()：主函数：1，创建参数解析器：parser，接着增加主函数执行的参数比如 --frames:打印帧数，--interval：打印执行间隔时间, --output:输出log.txt文件，保存读取的距离和温度。
通过for frame in range(args.frames) 遍历帧数，读取传感器的温度，距离和是否警告信息，最终都写入到line = format_reading(frame, distance, temperature, warning),每一帧都包含了distance,temp, status。然后append 到列表中去。每次间隔0.5s。
args.output.write_text 则负责把lines这个记录好的列表放到sensor_log.txt文件里




## Code I Wrote Today

- 

## Bugs / Problems

-  改 0.8m 后 WARNING 比 1.0m 更少，符合预期（阈值更低更严格）。
若两次独立运行对比，因距离随机，具体次数会波动；用固定 random.seed 或增大 --frames 可更清楚看到差异。

- 固定随机种子，random.seed(42)  # 两次运行用同一个 seed，距离序列相同

## How I Solved Them

- 用 `random.seed(42)` 固定距离序列；增大 `--frames` 可更稳定地对比 WARNING 次数

---

## English Summary

（下面由助手根据你的 Day 03 笔记起草，请朗读 2–3 遍，理解后再用自己的话复述。）

Today I worked on the Python fake sensor simulation in `sensor_sim.py`.

I learned how the `FakeSensor` class reads distance and temperature, checks warnings, and writes output to `sensor_log.txt`.

I changed the warning threshold from 1.0 m to 0.8 m. A lower threshold is stricter, so WARNING appears less often.

I also learned that random distance values make each run different. To compare fairly, I can use `random.seed(42)` or run more frames.

The program uses command-line arguments like `--frames` and `--interval` to control how many readings to print and how long to wait between them.

---

## Key Terms

（请对照中文理解；熟练后可遮住中文列自测。）

| English | 中文 |
|---------|------|
| class | 类（把数据和方法封装在一起） |
| constructor | 构造函数（Python 的 `__init__`） |
| method | 方法（类里的函数） |
| warning threshold | 告警阈值（距离小于该值时 WARNING） |
| random seed | 随机种子（固定后可重复同一随机序列） |
| command-line argument | 命令行参数（如 `--frames 10`） |
| sensor simulation | 传感器模拟（无真实硬件，用代码生成读数） |
| parse | 解析（程序读取并理解命令行参数） |

---

## What I Still Don't Understand

- 

## Tomorrow's Plan

1. 
2. 
3. 

## Git Commit

- Commit message：
- Pushed to GitHub：Yes / No
