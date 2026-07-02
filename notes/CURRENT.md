# 当前学习进度（每天只看这个文件）

> 更新规则：每完成一天，把「今天做」改成下一天的内容。

## 你现在的位置

- **阶段**：Month 1 / Week 1
- **已完成**：Day 01、Day 02（Linux + Git 练习）
- **今天**：Day 03 — Python class 升级版假传感器
- **本周目标**：打好工程基础，能独立跑 Python/C++ demo，周末定好 Ubuntu 虚拟机方案

## 今天做这 4 件事（Day 03）

### 1. 学（30 分钟）

打开 [`python_practice/sensor_sim.py`](../python_practice/sensor_sim.py)，对照代码回答（能说出来才算懂）：

- `FakeSensor` 这个 class 模拟了什么？
    模拟了传感器的温度，距离以及是否警告的变化
- `read_distance()` / `read_temperature()` / `is_warning()` 各做什么？
  1,`read_distance()` 表示读取传感器的距离
  2,`read_temperature()` 表示读取传感器的温度
  3,`is_warning()` 表示传感器是否警告
- `WARNING_DISTANCE_M = 1.0` 表示什么？什么时候会打印 `WARNING`？
  1,表示警告距离，当传感器离目标小于1米时发出警告
  2,当warning为true时

### 2. 练（30 分钟）

先跑通：

```bash
cd "/Users/ganggang/Documents/Robotics Learning/python_practice"
python3 sensor_sim.py --frames 10 --interval 0.5
cat sensor_log.txt
```

再自己改需求（今天必做）：

1. 打开 `sensor_sim.py`
2. 把 `WARNING_DISTANCE_M` 从 `1.0` 改成 `0.8`
3. 再运行一次，对比 WARNING 出现次数有没有变化

可选：多跑几次 `--frames 20`，观察 0.8m 和 1.0m 的差别。

修改对比发现，改成0.8与1并没有明显区别，因为每次到distance具有随机性，所以小于1或者0.8的warning有时候多有时候少
### 3. 记（15 分钟）

填写 [`notes/day03.md`](day03.md)：

- 每个 class 方法的作用（用自己的话）
- 改 0.8m 之后观察到什么
- 今天遇到的 bug

### 4. 提交（5 分钟）

```bash
cd "/Users/ganggang/Documents/Robotics Learning"
git add python_practice/sensor_sim.py notes/day03.md notes/CURRENT.md
git commit -m "Day 03: Python FakeSensor class and warning threshold change"
git push
```

## 今天完成标准

- [x] 能独立运行 `python3 sensor_sim.py` 并看到终端输出
- [x] 能说出 `FakeSensor` 三个方法各自干什么
- [x] 已把告警距离改成 0.8m 并重新运行对比
- [x] `notes/day03.md` 已填写
- [x] 今天有 Git commit

## 明天（Day 04 预告）

- 编译运行 C++ 版 `FakeSensor`（`cpp_practice/fake_sensor_cpp/`）
- 对照 Python 版，理解 `.hpp` / `.cpp` 怎么分工
- 填写 `notes/day04.md`

## 本周完整日程

见 [`notes/week1-schedule.md`](week1-schedule.md)

## 每天固定节奏

```
看一点(30min) → 练一点(30min) → 记笔记(15min) → git commit(5min)
```

## 学不好时问自己

1. 我今天写代码 / 敲命令了吗？ Yes
2. 我运行并看到结果了吗？ Yes
3. 我改过一个地方吗？ Yes
4. 我记下来了吗？Yes

四个都是 Yes，才算有效的一天。
