# Robotics & Engineering Glossary

英中对照词汇表。每天从当日日志 **Key Terms** 抄录新词；每周读 1 份英文 JD 时把不懂的词也加进来。

**规则：**
- 只记当天真正用到的词，不堆砌
- 格式：`| English term | 中文 | 简短例句或备注 |`
- Week 1 目标：约 40–50 词；Month 1 目标：约 80 词

---

## Day 01 — Fake Distance Sensor Demo

| English | 中文 | Note |
|---------|------|------|
| distance sensor | 距离传感器 | Measures how far an object is |
| sensor reading | 传感器读数 | A single measurement from a sensor |
| simulation | 模拟 | Fake data instead of real hardware |
| random distance value | 随机距离值 | Used in our fake sensor demo |
| CMake | C++ 构建工具 | Generates build files for C++ |
| executable | 可执行文件 | `./fake_sensor` after `make` |
| build process | 编译构建流程 | configure → compile → link → run |
| continuous data | 连续数据 | Sensors stream readings over time |
| safety threshold | 安全阈值 | Distance below which we warn |
| obstacle detection | 障碍物检测 | Detecting objects in the robot's path |

---

## Day 02 — Linux & Git

| English | 中文 | Note |
|---------|------|------|
| terminal | 终端 | Command-line interface for Linux |
| working directory | 工作目录 | Current folder (`pwd` shows it) |
| redirect | 重定向 | `>` overwrite file, `>>` append |
| grep | 搜索文件内容 | Find text inside files |
| git status | 查看 Git 状态 | Shows modified / staged / untracked files |
| staging area | 暂存区 | After `git add`, before `git commit` |
| git diff | 查看未暂存改动 | Compares working tree vs staging area |
| git diff --staged | 查看已暂存改动 | Compares staging area vs last commit |
| commit | 提交 | Save a snapshot to Git history |
| HEAD | 当前提交指针 | Not a command — marks where you are |

---

## Day 03 — Python Class

| English | 中文 | Note |
|---------|------|------|
| class | 类 | Groups data and methods together |
| constructor | 构造函数 | Python: `__init__`; sets up the object |
| method | 方法 | A function inside a class |
| warning threshold | 告警阈值 | Distance below which status = WARNING |
| random seed | 随机种子 | Same seed → same random sequence |
| command-line argument | 命令行参数 | e.g. `--frames 10 --interval 0.5` |
| sensor simulation | 传感器模拟 | Fake readings without real hardware |
| parse | 解析 | Read and interpret CLI arguments |

---

## Day 04 — C++ Class

| English | 中文 | Note |
|---------|------|------|
| header file | 头文件 | `.hpp` — declares classes and methods |
| source file | 源文件 | `.cpp` — implements the logic |
| declaration | 声明 | What exists (signatures, members) |
| implementation | 实现 | How methods actually work |
| compile | 编译 | Turn source code into machine code |
| link | 链接 | Combine `.o` files into one executable |
| encapsulation | 封装 | Hide internals with `private` |
| member variable | 成员变量 | Object state, e.g. `gen_` |
| const member function | 常量成员函数 | Promises not to modify object state |
| random engine | 随机引擎 | e.g. `std::mt19937` in our sensor |

---

## Day 05 — Repo Hygiene

| English | 中文 | Note |
|---------|------|------|
| gitignore | Git 忽略规则文件 | Tells Git which files not to track |
| build artifact | 编译产物 | e.g. `build/`, compiled binaries |
| source code | 源代码 | Human-readable `.py`, `.cpp`, `.hpp` files |
| repository | 代码仓库 | This project's GitHub repo |
| README | 项目说明文档 | How to build and run the project |
| version control | 版本控制 | Managing code changes with Git |
| regenerate | 重新生成 | Logs and build outputs can be recreated |
| metadata | 元数据 | e.g. `.DS_Store` — not project source code |

---

## Day 06 — Environment Setup

（学完 Day 06 后在此追加）

---

## Day 07 — Week 1 Review

（学完 Day 07 后在此追加）

---

## JD Vocabulary（从招聘启事积累）

| English | 中文 | Source |
|---------|------|--------|
| | | |
