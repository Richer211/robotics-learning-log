# Linux + Git 速查（Week 1 必会）

每天练 10 分钟，直到不用看也能敲出来。

---

## Linux 文件与目录

| 命令 | 作用 | 示例 |
|------|------|------|
| `pwd` | 显示当前路径 | `pwd` |
| `cd` | 进入目录 | `cd python_practice` |
| `cd ..` | 返回上一级 | `cd ..` |
| `ls` | 列出文件 | `ls` |
| `ls -la` | 列出所有文件（含隐藏） | `ls -la` |
| `mkdir -p` | 创建文件夹（可嵌套） | `mkdir -p a/b/c` |
| `touch` | 创建空文件 | `touch test.txt` |
| `cat` | 查看文件内容 | `cat test.txt` |
| `cp` | 复制 | `cp a.txt b.txt` |
| `mv` | 移动或重命名 | `mv old.txt new.txt` |
| `rm` | 删除文件 | `rm test.txt` |
| `grep` | 在文件中搜索 | `grep warning log.txt` |
| `echo` | 输出文本（常配合重定向写文件） | `echo "distance=1.2"` |
| `>` | 重定向：把输出**写入**文件（覆盖原内容） | `echo "a=1" > data.txt` |
| `>>` | 重定向：把输出**追加**到文件末尾 | `echo "a=2" >> data.txt` |

`>` 与 `>>` 不只用于 `echo`，任何命令的标准输出都可以重定向到文件，例如 `ls -la > listing.txt`。

**`echo` + 重定向示例**（模拟传感器写读数）：

```bash
echo "distance=1.2" > sensor.txt   # 新建/覆盖，文件里只有一行
echo "distance=0.5" >> sensor.txt  # 追加，文件里变成两行
cat sensor.txt
# distance=1.2
# distance=0.5
```

### 小练习

```bash
mkdir -p ~/robotics-test/day02
cd ~/robotics-test/day02
echo "distance=1.2" > sensor.txt
echo "distance=0.5" >> sensor.txt
grep "0.5" sensor.txt
```

---

## Git 日常工作流

| 命令 | 作用 |
|------|------|
| `git status` | 看哪些文件改了 |
| `git diff` | 看具体改了什么 |
| `git add <file>` | 把文件加入暂存区 |
| `git add .` | 暂存所有改动（小心使用） |
| `git commit -m "msg"` | 提交 |
| `git push` | 推到 GitHub |
| `git log --oneline` | 看提交历史 |
| `git branch` | 看分支 |

### 你每天学习结束固定执行

```bash
git status
git add <你改的文件>
git commit -m "Day XX: 一句话说明今天做了什么"
git push
```

### 好的 commit message 例子

- `Day 02: Linux and Git practice notes`
- `Day 03: Python FakeSensor class with warning threshold`
- `Day 04: C++ FakeSensor class refactor`

---

## 和机器人学习的关系

- **Linux**：机器人开发几乎都在 Linux 上跑（ROS2、仿真、部署）
- **Git**：公司项目、开源机器人代码、你的作品集都在 GitHub
- 现在练熟，后面学 ROS2 不会同时被命令行拖住
