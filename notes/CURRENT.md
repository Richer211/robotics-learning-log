# 当前学习进度（每天只看这个文件）

> 更新规则：每完成一天，把「今天做」改成下一天的内容。

## 你现在的位置

- **阶段**：Month 1 / Week 1
- **已完成**：Day 01～04（Python/C++ 假传感器、Linux/Git、Python class、C++ class + CMake）
- **今天**：Day 05 — 工程规范（`.gitignore` + README）
- **本周目标**：打好工程基础，能独立跑 Python/C++ demo，周末定好 Ubuntu 虚拟机方案

## 今天做这 5 件事（Day 05）

### 1. 学（30 分钟）

打开仓库根目录的 [`.gitignore`](../.gitignore)，对照回答（答案写在 [`notes/day05.md`](day05.md)）：

- 为什么 `build/` 和 `**/build/` 要忽略？
- 为什么 `sensor_log.txt` 要忽略？
- `__pycache__/`、`.DS_Store` 分别是什么？为什么要忽略？
- Day 04 编译出的 `practice/day04/random_demo`（无扩展名的二进制）应不应该提交？为什么？

再快速浏览 [`README.md`](../README.md) 的 **Build & Run (Week 1)** 一节，弄清 Python / C++ 的正式运行命令写在哪。

### 2. 练（30 分钟）

**不看笔记**，按 README 从头跑一遍两个 demo：

```bash
# Python
cd "/Users/ganggang/Documents/Robotics Learning/python_practice"
python3 sensor_sim.py --frames 10 --interval 0.5

# C++（README 标准流程）
cd "/Users/ganggang/Documents/Robotics Learning/cpp_practice/fake_sensor_cpp"
mkdir -p build && cd build
cmake ..
make
./fake_sensor
```

然后检查 Git 是否干净（没有误加编译产物）：

```bash
cd "/Users/ganggang/Documents/Robotics Learning"
git status
```

可选实践：在 `.gitignore` 里加一行，忽略练习目录下的本地二进制（例如 `practice/**/random_demo`），避免以后再误提交。

### 3. 记中文笔记（10 分钟）

填写 [`notes/day05.md`](day05.md) 的 **中文总结** 部分：

- `.gitignore` 里至少 3 条规则的含义（用自己的话）
- README 构建命令你是否能独立跑通
- `git status` 里有没有不该跟踪的文件

### 4. 写英文输出（10 分钟）

在同一文件填写（Week 1 每天必做）：

1. **English Summary**（3–5 句，用简单英文）
2. **Key Terms**（3–8 个，如 `gitignore`, `build artifact`, `repository`, `README`）
3. 新词抄到 [`notes/glossary/robotics-terms.md`](glossary/robotics-terms.md) 的 Day 05 区

**Week 1 今天不必做：** 60-second Speaking、Interview Q&A

模板见 [`notes/templates/daily-log.md`](templates/daily-log.md)；范例见 [`notes/day01.md`](day01.md)。

### 5. 提交（5 分钟）

```bash
cd "/Users/ganggang/Documents/Robotics Learning"
git add notes/day05.md notes/CURRENT.md notes/glossary/robotics-terms.md
# 若改了 .gitignore 或 README，一并 add
git commit -m "Day 05: document gitignore and README build steps"
git push
```

> Git commit 一律用英文。

## 今天完成标准

- [ ] 能解释为什么 `build/` 不应提交 Git
- [ ] 能按 README 独立跑通 Python 和 C++ demo
- [ ] `git status` 里没有 `build/`、二进制、`sensor_log.txt` 等误跟踪文件
- [ ] `notes/day05.md` 中文总结已填写
- [ ] `notes/day05.md` 有 English Summary + Key Terms
- [ ] 今天有英文 Git commit

## 英文学习分阶段（不用一次做完）

| 阶段 | 每天英文任务 |
|------|----------------|
| **Week 1（Day 02–07）** | English Summary + Key Terms（+10 min） |
| **Week 2 起** | 加上 60-second Speaking Draft（可先读稿） |
| **Week 3 起** | 每周 2 次 Interview Q&A（周五或完成一周项目时） |
| **Month 2 起** | 录音 + 复盘，见 [`notes/speaking/README.md`](speaking/README.md) |

原则：**中文理解技术，英文沉淀表达；技术是主线，英文每天 +10 分钟。**

## 明天（Day 06 预告）

- `docker run hello-world`（如已装 Docker）
- 阅读并按步骤开始 [`notes/environment.md`](environment.md) 的 VM 安装
- 填写 `notes/day06.md`（含 English Summary + Key Terms）

## 本周完整日程

见 [`notes/week1-schedule.md`](week1-schedule.md)（含每日建议 Key Terms）

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
