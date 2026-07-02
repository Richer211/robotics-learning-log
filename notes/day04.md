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

- [ ] 

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

## Git Commit

- Commit message：
- Pushed to GitHub：Yes / No
