# Day 02 - Robotics Learning

> 状态：**完成** — 请今天亲手完成后打勾。

## Today's Goal

- [x] 练习 Linux 基础命令（见 `notes/cheatsheets/linux-git.md`）
- [x] 复习 Git 工作流（status / add / commit / push / log）
- [x] 填写本日志

## What I Finished

- [x] 在终端完成了 `practice/day02/` 里的文件操作练习
- [x] 运行了 `git status` 和 `git log --oneline`
- [x] 填写了「What I Learned」和「Bugs」

## What I Learned

- 完成linxu-git.md中的手写练习
- 完成day02.md中的linux和git的实操练习

## Code I Wrote Today

- `practice/day02/hello.txt`（Linux 文件操作练习）

## Bugs / Problems

- 对于grep,ls -la,echo > >>,git diff, git log --oneline, mv, touch这些命令还不熟

## How I Solved Them

-  多练习，grep 是搜查文件内容，ls -la是展示当前目录下的所有文件包括隐藏文件，echo '' >  .txt 是把某个内容全覆盖进某个文件，echo "" >> .txt 是把某个内容加入到某个文件末尾， git diff --staged必须是已经加入缓存区的文件但是还没再改过； 而git diff -> 表示提交缓存区之后又改过， git log --oneline 是看出当前所有提交的日志记录，mv 是把某个文件移动或重命名为新文件， touch 是创建一个新的空文件

- git diff 不只是「add 之后又改过」
对已跟踪文件（比如 notes/day02.md），改了但从来没 git add，也会出现在 git diff 里——你终端最后那段 day02.md 就是这样。

改了文件，没 add     →  git diff 能看到
改了文件，add 了     →  git diff 空（暂存区和工作区一致）
add 之后又改        →  git diff 看到「多出来的那部分」
- git diff --staged 不只是「add 后没再改过」
只要文件在暂存区里（git add 过、还没 commit），就能看——不管之后有没有再改。

add 后没再改 → --staged 显示全部 staged 内容，git diff 为空
add 后又改 → --staged 仍是 add 那一刻 的内容；git diff 是 add 之后又多出来的改动

## Git diff 口诀（实操总结）

三个区域的关系：

```
上次 commit  ←── git diff --staged ──→  暂存区  ←── git diff ──→  工作区（正在编辑的文件）
              （准备提交的）                    （还没再次 add 的改动）
```

| 命令 | 比较的是什么 |
|------|----------------|
| `git diff` | **工作区** vs **暂存区**（改了但还没 `git add`，或 `add` 之后又改过、还没再次 `add`） |
| `git diff --staged` | **暂存区** vs **上次 commit**（已经 `git add`、准备提交的内容） |

常见情况：

| 情况 | `git diff` | `git diff --staged` |
|------|------------|---------------------|
| 新文件，从未 `git add` | ❌ 看不到 | ❌ 看不到 → 用 `git status` + `cat` |
| 改了文件，没 `add` | ✅ 能看到 | ❌ |
| 改了文件，`add` 了，没再改 | 空 | ✅ 能看到 |
| `add` 之后又改 | ✅ 只看到多出来的部分 | ✅ 仍是 `add` 那一刻的内容 |

实操口诀：

| 你做了什么 | 该用什么 |
|------------|----------|
| 新建文件/文件夹，没 `add` | `git status`，`cat 文件路径` |
| `git add` 之后，想看将要提交什么 | `git diff --staged` |
| `add` 之后又改了，没再 `add` | `git diff`（或 `git diff -- 文件路径`） |
| 想一次看所有未 commit 的改动 | `git diff HEAD` |

## 查看历史 commit 常用命令

`HEAD` 是指针（当前所在位置），**不是命令**。`git log` 里的 `(HEAD -> main)` 表示当前在 `main` 分支最新提交上。

❌ 错误：`git HEAD 73c853a`（没有 `git HEAD` 这个命令）

| 目的 | 正确命令 |
|------|----------|
| 看提交历史（简版） | `git log --oneline` |
| 看某次提交详情 | `git show 73c853a` |
| 和某次提交对比当前改动 | `git diff 73c853a` |
| 临时切到某次提交看看（只读） | `git checkout 73c853a` |
| 回到最新 `main` | `git checkout main` |

## 删除文件/文件夹（Git）

### 未跟踪（`git status` 显示 `??`）

Git 不管这类文件，用普通删除：

```bash
rm notes/old.txt      # 删单个文件
rm -r a/              # 删整个文件夹
```

### 已跟踪（已在仓库里）

用 `git rm`，从磁盘和 Git 记录里一起删：

```bash
git rm practice/day02/backup.txt    # 删单个文件
git rm -r a/                          # 删整个文件夹
git commit -m "Remove unused files"
git push
```

已经用 `rm` 手动删了：

```bash
git rm a/f.txt          # 或 git add -u
git commit -m "Remove unused files"
```

### 只从 Git 移除，保留本地文件

```bash
git rm --cached a/test.txt    # 单个文件
git rm -r --cached a/         # 整个文件夹
echo "a/" >> .gitignore
git add .gitignore
git commit -m "Stop tracking a/ folder"
```

### 删错了、还没 commit — 恢复

```bash
git restore practice/day02/backup.txt
git restore --staged a/f.txt
git restore a/f.txt
```

### 快速对照

| 情况 | 命令 |
|------|------|
| 新文件/文件夹，从没 `git add` | `rm` 或 `rm -r` |
| 已跟踪，磁盘和 Git 都删掉 | `git rm` / `git rm -r` → `commit` |
| 已跟踪，只不想 Git 管了 | `git rm --cached` + `.gitignore` |
| 删错了，还没 commit | `git restore 文件路径` |

### `git rm` 报错怎么办？

`add` 了但没 `commit`，或 `add` 之后又改过，`git rm -r` 可能报错：

```
error: the following file has staged content different from both the file and the HEAD
(use -f to force removal)
```

这是 Git 在保护未提交的改动。练习文件夹确定不要了，强制删除：

```bash
git rm -rf a/
```

或先撤出暂存区再普通删除：

```bash
git restore --staged a/
rm -r a/
```

**记住**：`rm` = 只删本地；`git rm` = 删本地 + 告诉 Git 下次 commit 时从仓库移除。

## What I Still Don't Understand

-  No

## Tomorrow's Plan

1. 跑 Python 升级版假传感器 `python_practice/sensor_sim.py`
2. 自己把告警距离从 1.0m 改成 0.8m
3. 填写 `notes/day03.md`

## Git Commit

- Commit message：今日day 02 的改动提交
- Pushed to GitHub：Yes
