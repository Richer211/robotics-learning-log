# Day 04 - Robotics Learning

> 状态：**已完成**

## Today's Goal

- [x] 编译运行 C++ `FakeSensor` class 版本
- [x] 对照 Python 版，理解 .hpp / .cpp 分工

## 运行命令

```bash
cd cpp_practice/fake_sensor_cpp
mkdir -p build && cd build
cmake .. && make && ./fake_sensor
```

## What I Finished

- [x] 「完成 random_demo 练习」

## What I Learned

### C++ 的 `FakeSensor` 和 Python 版各有哪些方法？一一对应关系是什么？
-  class FakeSensor <-> FakeSensor
-  read_distance() <-> readDistance()
-  read_temperature(self) <-> readTemperature()
-  is_warning() <-> isWarning()
-  format_reading() <-> formatReading()


### `.hpp` 和 `.cpp` 为什么要分开？（提示：声明 vs 实现）
- hpp主要用来声明方法和变量，cpp主要用来实现具体的方法
### `WARNING_DISTANCE_M` 在 C++ 里写在哪？和 Python 的 `class` 变量有何异同？
- 写在hpp里的static constexpr double WARNING_DISTANCE_M = 1.0;
- 区别在于一个写在class内部作为全局变量，python的声明函数和具体实现都写在一个python文件里，而c++则把声明和实现分开，而这种全局的固定变量则写在hpp里
### `main.cpp` 和 Python 的 `main()` 流程有什么不同？
- 一个专门写在了cpp文件里，一个则写在python文件里，没有单独区分
- main.cpp和main()内部的写法有差异，尤其关于如何把打印出来的信息写入到sensor_log.txt，main()会创建参数解析器，然后把return出来的信息比如frame，distance,temp,status打印出来，而main.cpp则直接用std::cout << line << std::endl;主要在于写法不一样。

## C++ 编译过程（总结）

### 改代码后要不要重新编译？

**要。** C++ 是编译型语言，改完 `.cpp` / `.hpp` 后必须 `make` 再运行，否则跑的还是旧程序。

| 语言 | 改代码后 |
|------|----------|
| Python | 直接 `python3 xxx.py` |
| C++ | `make` → `./fake_sensor` |

### 编译在干什么？

```
源码 (.cpp / .hpp)  →  编译 + 链接  →  可执行文件 (./fake_sensor)
   人能读的文本                         CPU 能跑的二进制
```

- **源码** = 菜谱（人看）
- **编译** = 按菜谱做成菜
- **运行** = 吃成品；只改菜谱不重新做，端上来的还是旧菜

### 本项目的三步命令

```bash
cd cpp_practice/fake_sensor_cpp/build
cmake ..          # 配置：读 CMakeLists.txt，生成 Makefile（通常只需一次）
make              # 编译 + 链接：.cpp → .o → fake_sensor
./fake_sensor     # 运行可执行文件
```

| 步骤 | 作用 | 什么时候要重做 |
|------|------|----------------|
| `cmake ..` | 配置构建规则 | 第一次建 `build/`；或改了 `CMakeLists.txt` |
| `make` | 编译改动的 `.cpp`，链接成可执行文件 | **每次改 C++ 源码后** |
| `./fake_sensor` | 运行程序 | 每次想看到新结果时 |

### 编译 vs 链接

**编译**：每个 `.cpp` 单独变成 `.o`（机器码片段）

```
main.cpp        →  main.cpp.o
fake_sensor.cpp →  fake_sensor.cpp.o
```

`.hpp` 不单独编译，通过 `#include` 被 `.cpp` 包含进去。

**链接**：把多个 `.o` 拼成一个可执行文件

```
main.cpp.o + fake_sensor.cpp.o  →  fake_sensor
```

`make` 会做**增量编译**：只重编改过的文件，比全量编译快。

### 改不同文件怎么办？

| 改了什么 | 需要做什么 |
|----------|------------|
| `main.cpp` / `fake_sensor.cpp` / `.hpp` | `make` → `./fake_sensor` |
| `CMakeLists.txt` | `cmake ..` → `make` → `./fake_sensor` |

### 和 Python 对照

| | Python | C++ |
|---|--------|-----|
| 执行方式 | 解释执行 | 先编译再执行 |
| 改代码后 | 直接再跑 | 先 `make` 再跑 |
| 产物 | 无单独二进制 | `build/fake_sensor` |

### 为什么 `build/` 不提交 Git？

`build/` 是编译产物，可从源码用 `cmake && make` 重新生成，所以写在 `.gitignore` 里。仓库只提交 `.cpp` / `.hpp` 等源码即可。

**口诀**：改 C++ 源码 → `make` → 再运行；`cmake ..` 只在第一次或改构建配置时需要。

### 和 Python 版对照后，你理解了什么
- C++的编译和功能区分更严格，会把main函数，hpp，cpp分开，而python则全部写在一起
- 但是两个版本的实现逻辑是一致的，都是先建class传感器，传感器内部定义方法,接着就是在main函数里去实现具体的步骤，main()内部一般只有定义变量和调用方法。

### cmake && make 过程中有没有报错
- 没有报错，cmake主要用来配置环境，主要是CMakeLists.txt出现变化时，需要重新配置，决定编译哪些文件，用什么编译器，输出叫什么，这些都会在CMakeLists.txt体现，而cmake ..则是一个配置开关。
- make则一般当C++文件修改后，需要重新编译，把cpp文件也就是人看的代码，编译成机器看的文件，也就是.cpp.o。

## C++ 核心概念最小笔记

### 类名 vs 构造函数

| 名字 | 是什么 |
|------|--------|
| `FakeSensor` | **类名**（≈ Python `class FakeSensor:`） |
| `FakeSensor::FakeSensor(...)` | **构造函数**（≈ Python `def __init__(self, ...)`） |

C++ 构造函数**必须和类同名**；Python 固定叫 `__init__`。

一个类可以有**多个构造函数**（参数不同），不是「有且唯一」。本项目目前只定义了一个。多个构造函数 = 同名（类名）+ 不同参数；不是多个不同名字的「构造函数」。

### `private` 成员：内部零件

```cpp
private:
  std::mt19937 gen_;
  std::uniform_real_distribution<> distanceDist_;
  std::uniform_real_distribution<> temperatureDist_;
```

- 在 `.hpp` 里**声明**成员类型和名字
- 在 `.cpp` 构造函数里用 `:` 初始化列表赋初值
- **类外部不能直接访问**（`main.cpp` 里写 `sensor.gen_` 会编译报错）
- 外面只能通过 `public` 方法使用，例如 `readDistance()`、`seed(42)`

封装 = 实现细节藏起来，只暴露必要接口。

### `<random>`：随机数怎么工作

Python 一行：

```python
random.uniform(0.1, 5.0)
```

C++ 拆成**发动机 + 分布规则**：

| 类型 | 作用 | 本项目 |
|------|------|--------|
| `std::mt19937` | 伪随机数**引擎**（产生随机性） | `gen_` |
| `std::uniform_real_distribution<>` | **均匀浮点分布** [min, max] | `distanceDist_`、`temperatureDist_` |

读一次距离：

```cpp
return distanceDist_(gen_);   // 用分布规则，从引擎里抽一个数
```

构造函数里三行初始化：

```cpp
: gen_(std::random_device{}()),           // 启动随机引擎（系统随机种子）
  distanceDist_(minDistance, maxDistance), // 距离范围 0.1～5.0
  temperatureDist_(18.0, 35.0)             // 温度范围 18～35
```

设固定种子（可重复实验）：

```cpp
sensor.seed(42);   // 内部调用 gen_.seed(42)
// 不能写 random.seed(42) —— C++ 没有 Python 那种全局 random 模块
```

**口诀**：引擎产生随机性，分布规定范围；`dist(gen)` 就是一次读取。

### 最小练习代码（可单独编译理解）

文件路径：`practice/day04/random_demo.cpp`

```cpp
#include <iostream>
#include <random>

int main() {
    std::mt19937 gen(42);
    std::uniform_real_distribution<> dist(0.1, 5.0);
    for (int i = 0; i < 5; ++i)
        std::cout << dist(gen) << "\n";
}
```

**怎么单独编译运行**（不用 cmake，单文件即可）：

```bash
cd practice/day04
g++ -std=c++17 random_demo.cpp -o random_demo
./random_demo
```

改源码后必须重新 `g++` 再运行，否则跑的还是旧程序。

#### `random_demo` 在干什么（精确理解）

1. `std::mt19937 gen(42)` — 创建**随机引擎**，`42` 是种子（起点）
2. `std::uniform_real_distribution<> dist(0.1, 5.0)` — 创建**分布规则**（范围 0.1～5.0）
3. `dist(gen)` — 从 `gen` 取随机性，经 `dist` **变换**成区间内的一个浮点数

> **`gen` = 发动机（提供随机性）；`dist` = 范围规则；不是 dist「让 gen 落在范围内」，而是 `dist(gen)` 一次读数。**

与 `FakeSensor` 对应：

```cpp
return distanceDist_(gen_);   // 就是 random_demo 里的 dist(gen)
```

#### 种子（seed）是什么意思

| 概念 | 含义 |
|------|------|
| 种子 | 随机引擎的**起点** |
| 相同种子 | 每次运行 → **完全相同**的数列（可重复实验） |
| 不同种子（如 42 vs 99） | 数列**不同**，但每个数仍在 `dist` 规定的范围内 |

对比实验时要**固定种子**，只改别的参数（如 `WARNING_DISTANCE_M`），才公平。

**实验**：把 `gen(42)` 改成 `gen(99)` → 保存 → `g++` 重新编译 → `./random_demo`，输出应与 42 时不同；改回 42 再编译，应和第一次 42 时完全一样。

### 和 Python 对照表

| Python | C++ |
|--------|-----|
| `class FakeSensor` | `class FakeSensor` |
| `def __init__(self, ...)` | `FakeSensor::FakeSensor(...)` |
| `random.uniform(a, b)` | `uniform_real_distribution<>(a,b)(gen_)` |
| `random.seed(42)` | `sensor.seed(42)` → `gen_.seed(42)` |
| 全写在一个 `.py` 文件 | `.hpp` 声明 + `.cpp` 实现 |

### 对象状态、`FakeSensor::` 与 `const`

#### 数据 vs 行为：什么是「对象状态」？

| 类型 | 例子 | 是不是状态 |
|------|------|------------|
| **成员变量**（数据） | `gen_`、`distanceDist_`、`temperatureDist_` | ✅ 是 |
| **成员函数**（行为） | `readDistance()`、`seed()`、`isWarning()` | ❌ 不是 |
| **构造函数** | `FakeSensor::FakeSensor(...)` | ❌ 不是；负责**建立**初始状态 |

- **对象** = 一个实例，例如 `main` 里的 `FakeSensor sensor`
- **对象状态** = 这个实例里成员变量**当前的值**
- 本项目里状态都在 `private` 的三个 `_` 变量里（习惯上状态放 private，外面用 public 方法操作）

`static constexpr WARNING_DISTANCE_M` 是类级常量，不算每个对象各自变化的状态。

#### `FakeSensor::` 是什么意思？

`::` 是**作用域解析符**，表示「属于 `FakeSensor` 这个类」——**不是**「状态」的意思。

```cpp
FakeSensor::readDistance()   // FakeSensor 类的 readDistance 方法实现
FakeSensor::FakeSensor(...)  // FakeSensor 类的构造函数实现
```

声明在 `.hpp`，实现写在 `.cpp` 时必须在函数名前加 `FakeSensor::`。

#### 构造函数 vs 对象状态

| | 构造函数 | `const` 成员函数 |
|---|----------|------------------|
| 时机 | 对象**刚创建**时，一次 | 对象**已存在**后，每次调用 |
| 作用 | **初始化** `gen_` 等成员（建立状态） | 在**不修改**成员的前提下查询/计算 |

```cpp
: gen_(std::random_device{}()),
  distanceDist_(minDistance, maxDistance),
  temperatureDist_(18.0, 35.0)
```

这三行是在对象「出生时」把状态装好。

#### 多个构造函数（重载）

构造函数**名字必须 = 类名**，多个版本只靠**参数不同**区分：

```cpp
FakeSensor();                                    // 无参
FakeSensor(double min, double max);              // 本项目用的
FakeSensor(double min, double max, unsigned seed);
```

Python 用一个 `__init__(self, a=..., b=...)` + 默认参数；C++ 常写多个同名构造函数。

#### `const` 成员函数

```cpp
bool isWarning(double distance) const;
std::string formatReading(...) const;
```

函数后面的 `const` = 承诺**不修改这个对象的成员变量**（只读/查询）。

| 方法 | 有 `const`？ | 原因 |
|------|-------------|------|
| `isWarning`、`formatReading` | ✅ | 只比较/拼字符串，不改 `gen_` 等 |
| `readDistance`、`readTemperature`、`seed` | ❌ | 会改变 `gen_` 内部状态 |

**调用规则**：

| 谁调用谁 | 行不行 |
|----------|--------|
| `const` 方法 → `const` 方法 | ✅（`formatReading` 调 `isWarning`） |
| `const` 方法 → 非 `const` 方法 | ❌ |
| 非 `const` 方法 → `const` 方法 | ✅ |

可以不加 `const` 也能跑，但加了能表达「只读」、并允许在 `const` 对象和 `const` 方法里调用。

**口诀**：数据是状态，函数是行为；`FakeSensor::` 表归属，不表状态；`const` 方法只看不改。

### Week 1 够用 vs 以后再看

**现在掌握（本项目已出现）**：

- `std::mt19937`、`std::uniform_real_distribution<>`
- `std::random_device`（知道用来生成初始种子即可）
- 构造函数初始化列表 `:`
- `const` 成员函数（如 `formatReading(...) const` = 不修改对象状态）

**以后机器人/仿真可能遇到（用到再学）**：

| 类型 | 用途 |
|------|------|
| `std::normal_distribution<>` | 高斯噪声（传感器误差） |
| `std::vector<T>` | 点云、轨迹 |
| `std::chrono` | 时间间隔（`main.cpp` sleep 已在用） |

**不必现在系统学完**：整个 STL、所有分布类型、模板细节。

## Git Commit

- Commit message：learn day04.md
- Pushed to GitHub：Yes
