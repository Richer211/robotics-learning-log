# 当前学习进度（每天只看这个文件）

> 更新规则：每完成一天，把「今天做」改成下一天的内容。

## 你现在的位置

- **阶段**：Month 1 / Week 1
- **已完成**：Day 01～03（Python/C++ 初版、Linux/Git、Python class 假传感器）
- **今天**：Day 04 — C++ class 版 `FakeSensor` + CMake
- **本周目标**：打好工程基础，能独立跑 Python/C++ demo，周末定好 Ubuntu 虚拟机方案

## 今天做这 4 件事（Day 04）

### 1. 学（30 分钟）

打开 C++ 假传感器三个文件，对照 Python 版 [`python_practice/sensor_sim.py`](../python_practice/sensor_sim.py) 理解分工：

| 文件 | 作用 |
|------|------|
| `fake_sensor.hpp` | **声明**：class 有哪些方法、成员变量（头文件） |
| `fake_sensor.cpp` | **实现**：方法具体怎么写 |
| `main.cpp` | **入口**：`main()` 循环读传感器、打印、写日志 |

对照回答（能说出来才算懂）：

- C++ 的 `FakeSensor` 和 Python 版各有哪些方法？一一对应关系是什么？
- `.hpp` 和 `.cpp` 为什么要分开？（提示：声明 vs 实现）
- `WARNING_DISTANCE_M` 在 C++ 里写在哪？和 Python 的 `class` 变量有何异同？
- `main.cpp` 和 Python 的 `main()` 流程有什么不同？

### 2. 练（30 分钟）

编译并运行：

```bash
cd "/Users/ganggang/Documents/Robotics Learning/cpp_practice/fake_sensor_cpp"
mkdir -p build && cd build
cmake ..
make
./fake_sensor
cat sensor_log.txt
```

可选对比练习：

```bash
# 同一仓库里分别看 Python / C++ 日志
cat "/Users/ganggang/Documents/Robotics Learning/python_practice/sensor_log.txt"
cat sensor_log.txt
```

可选改需求（和 Day 03 呼应）：

1. 打开 `fake_sensor.hpp`，把 `WARNING_DISTANCE_M` 从 `1.0` 改成 `0.8`
2. 重新 `make && ./fake_sensor`，观察 WARNING 变化（记得：阈值越低，WARNING 越少）

### 3. 记（15 分钟）

填写 [`notes/day04.md`](day04.md)：

- `.hpp` / `.cpp` / `main.cpp` 各自干什么
- 和 Python 版对照后，你理解了什么
- `cmake && make` 过程中有没有报错

### 4. 提交（5 分钟）

```bash
cd "/Users/ganggang/Documents/Robotics Learning"
git add notes/day04.md notes/CURRENT.md
# 若改了 fake_sensor.hpp 等代码，一并 add
git commit -m "Day 04: C++ FakeSensor class and CMake build"
git push
```

> `build/` 目录不要提交（已在 `.gitignore` 里）。

## 今天完成标准

- [x] 能独立执行 `cmake .. && make && ./fake_sensor` 并看到输出
- [x] 能说出 `.hpp` 和 `.cpp` 的分工
- [x] 能对照 Python 版说出至少 3 个方法的对应关系
- [x] `notes/day04.md` 已填写
- [x] 今天有 Git commit

## 明天（Day 05 预告）

- 理解 `.gitignore` 为什么忽略 `build/`
- 确认 README 里的构建命令自己能跑通
- 填写 `notes/day05.md`

## 本周完整日程

见 [`notes/week1-schedule.md`](week1-schedule.md)

## 每天固定节奏

```
看一点(30min) → 练一点(30min) → 记笔记(15min) → git commit(5min)
```

## 学不好时问自己

1. 我今天写代码 / 敲命令了吗？
2. 我运行并看到结果了吗？
3. 我改过一个地方吗？
4. 我记下来了吗？

四个都是 Yes，才算有效的一天。
