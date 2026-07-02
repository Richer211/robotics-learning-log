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

- [ ] 

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

- 

## What I Still Don't Understand

- 

## Tomorrow's Plan

1. 
2. 
3. 

## Git Commit

- Commit message：
- Pushed to GitHub：Yes / No
