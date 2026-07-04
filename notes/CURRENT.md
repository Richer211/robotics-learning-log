# 当前学习进度（每天只看这个文件）

> 更新规则：每完成一天，把「今天做」改成下一天的内容。

## 你现在的位置

- **阶段**：Month 1 / Week 1
- **已完成**：Day 01～06（假传感器、Linux/Git、Python/C++ class、工程规范、Ubuntu VM）
- **今天**：Day 07 — Week 1 周复盘 + Ubuntu VM 收尾
- **本周目标**：复盘 Week 1，确认 Week 2 能在 Ubuntu VM 里开始 ROS2

## 今天做这 5 件事（Day 07）

### 1. 学（20 分钟）

回顾 Week 1 全部日志：

- [`notes/day01.md`](day01.md)：Python / C++ 假传感器初版
- [`notes/day02.md`](day02.md)：Linux + Git
- [`notes/day03.md`](day03.md)：Python class
- [`notes/day04.md`](day04.md)：C++ class + CMake
- [`notes/day05.md`](day05.md)：`.gitignore` + README workflow
- [`notes/day06.md`](day06.md)：Docker + Ubuntu VM

对照回答（写进 [`notes/weekly-review-w01.md`](weekly-review-w01.md)）：

- Week 1 你真正完成了哪些可运行产出？
- 你现在最熟的 3 个技能是什么？
- 你还不熟、Week 2 需要继续练的 3 个点是什么？
- Ubuntu VM 现在是否足够支撑 Week 2 学 ROS2？

### 2. 练（30 分钟）

在 Ubuntu VM 里做最后确认：

```bash
lsb_release -a
hostname -I
systemctl status ssh
```

如果还没退出 `systemctl status`，按 `q` 回到命令行。

可选：从 macOS 终端测试 SSH（把 IP 换成你的 VM IP，例如 `192.168.64.6`）：

```bash
ssh richard@192.168.64.6
```

如果 SSH 成功，输入 `exit` 退出。若不成功，先记录问题，不阻塞 Day 07。

### 3. 记中文复盘（20 分钟）

填写：

- [`notes/day07.md`](day07.md)
- [`notes/weekly-review-w01.md`](weekly-review-w01.md)

重点写：

- Week 1 完成了什么
- 哪些问题解决了
- 哪些内容仍不理解
- Week 2 的 Top 3 任务
- Ubuntu VM / Docker / Git / C++ 的当前状态

### 4. 写英文输出（10 分钟）

在 [`notes/day07.md`](day07.md) 或 [`notes/weekly-review-w01.md`](weekly-review-w01.md) 填写：

1. **English Summary**（3–5 句，简单英文）
2. **Key Terms**（3–8 个，建议：`weekly review`, `milestone`, `Ubuntu VM`, `ROS2 setup`, `next steps`）
3. 新词抄到 [`notes/glossary/robotics-terms.md`](glossary/robotics-terms.md) 的 Day 07 区

**Week 1 今天仍不必做：** 60-second Speaking、Interview Q&A

### 5. 提交（5 分钟）

```bash
cd "/Users/ganggang/Documents/Robotics Learning"
git add notes/day07.md notes/weekly-review-w01.md notes/CURRENT.md notes/glossary/robotics-terms.md
# 若 day06.md 还有 Ubuntu VM 最终状态更新，也一并 add
git commit -m "Day 07: review Week 1 and prepare ROS2 environment"
git push
```

> Git commit 一律用英文。

## 今天完成标准

- [ ] `notes/day07.md` 已填写
- [ ] `notes/weekly-review-w01.md` 已填写
- [ ] 能说出 Week 1 的主要产出和不足
- [ ] Ubuntu VM 状态已记录（版本、IP、SSH、桌面环境）
- [ ] Day 07 English Summary + Key Terms 已填写
- [ ] 今天有英文 Git commit

## 英文学习分阶段（不用一次做完）

| 阶段 | 每天英文任务 |
|------|----------------|
| **Week 1（Day 02–07）** | English Summary + Key Terms（+10 min） |
| **Week 2 起** | 加上 60-second Speaking Draft（可先读稿） |
| **Week 3 起** | 每周 2 次 Interview Q&A（周五或完成一周项目时） |
| **Month 2 起** | 录音 + 复盘，见 [`notes/speaking/README.md`](speaking/README.md) |

原则：**中文理解技术，英文沉淀表达；技术是主线，英文每天 +10 分钟。**

## 明天（Week 2 预告）

- 在 Ubuntu VM 里安装 / 验证 ROS2 Humble
- 进入 `week02_ros2_basics/ros2_ws`
- 学 ROS2 基础：node、topic、publisher、subscriber
- 开始填写 Week 2 学习日志

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
