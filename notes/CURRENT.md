# 当前学习进度（每天只看这个文件）

> 更新规则：每完成一天，把「今天做」改成下一天的内容。

## 你现在的位置

- **阶段**：Month 1 / Week 1
- **已完成**：Day 01（仓库 + Python/C++ 假传感器初版）
- **今天**：Day 02 — Linux 命令 + Git 复习
- **本周目标**：打好工程基础，能独立跑 Python/C++ demo，周末定好 Ubuntu 虚拟机方案

## 今天做这 4 件事（Day 02）

### 1. 学（30 分钟）

打开 [`notes/cheatsheets/linux-git.md`](cheatsheets/linux-git.md)，在终端里**亲手敲**每一行命令，不要只读。

### 2. 练（30 分钟）

```bash
cd "/Users/ganggang/Documents/Robotics Learning"
mkdir -p practice/day02
cd practice/day02
pwd
ls -la
echo "robotics day02" > hello.txt
cat hello.txt
grep robotics hello.txt
cp hello.txt hello_backup.txt
mv hello_backup.txt backup.txt
```

然后练 Git：

```bash
cd "/Users/ganggang/Documents/Robotics Learning"
git status
git log --oneline
git branch
```

### 3. 记（15 分钟）

填写 [`notes/day02.md`](day02.md)：
- 哪些命令记住了
- 哪些还不熟
- 今天遇到的 bug

### 4. 提交（5 分钟）

```bash
cd "/Users/ganggang/Documents/Robotics Learning"
git add notes/day02.md notes/cheatsheets/ practice/day02/hello.txt notes/CURRENT.md
git commit -m "Day 02 Linux and Git practice"
git push
```

## 今天完成标准

- [ ] 能不看文档使用：`cd` `ls` `pwd` `cat` `mkdir` `cp` `mv` `grep`
- [ ] 能不看文档使用：`git status` `git add` `git commit` `git push` `git log`
- [ ] `notes/day02.md` 已填写
- [ ] 今天有 Git commit

## 明天（Day 03 预告）

- 跑升级版 Python 假传感器（class + 告警 + 写文件）
- 自己改一个需求：把告警距离从 1.0m 改成 0.8m
- 填写 `notes/day03.md`

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
