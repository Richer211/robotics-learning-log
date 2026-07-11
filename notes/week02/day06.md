# Week 2 Day 06 - Modify ROS2 Demo Requirement

> 状态：**已完成** — 已完成参数小改动、重新 build/source/run，并在验证后恢复默认代码。

## Today's Goal

- [x] 对 Week 2 ROS2 demo 做一个小改动
- [x] 重新 build / source / run
- [x] 理解「改代码 → 重建 → 运行验证」的迭代流程

## 1. 学（20 分钟）

回顾：

- Week 1 Python/C++ 中的 `WARNING_DISTANCE_M`
- Week 2 publisher / subscriber 中的 `WARNING_DISTANCE_M`
- `colcon build --symlink-install` 后为什么还要 `source install/setup.bash`

回答：

- publisher 和 subscriber 里都有 warning threshold，会不会不一致？

会不一致。

`WARNING_DISTANCE_M` 不会被放进 `/sensor/distance` 的 message 里发送出去。

`/sensor/distance` 上传输的是 `sensor_msgs/Range` message，主要包含：

```text
header
radiation_type
field_of_view
min_range
max_range
range
```

也就是说，publisher 和 subscriber 通过 topic 传递的是距离值 `msg.range`，不是 warning threshold。

所以：

```text
publisher 的 WARNING_DISTANCE_M 只影响 publisher 自己什么时候打印 WARNING。
subscriber 的 WARNING_DISTANCE_M 只影响 subscriber 自己什么时候打印 WARNING。
```

如果 publisher 是 `1.0`，subscriber 是 `0.8`，那么 `0.9m` 这种距离可能会让 publisher 打印 warning，但 subscriber 不打印 warning。

- 如果只改 subscriber，系统行为会怎么变化？

如果只把 subscriber 里的 `WARNING_DISTANCE_M` 从 `1.0` 改成 `0.8`，subscriber 仍然会接收所有 `/sensor/distance` message。

变化只是：subscriber 只有在 `msg.range < 0.8` 时才打印 `WARNING`。

如果 publisher 的阈值仍然是 `1.0`，就会出现 publisher 和 subscriber 的 warning 输出标准不一致。

- 如果改 publisher 的 timer 从 `0.5` 到 `0.2`，输出频率会怎么变化？
输出频率会从0.5s发送一次变成0.2s发送一次，频率变快。
## 2. 练（40 分钟）

任选一个小改动：

- 把 warning threshold 从 `1.0` 改成 `0.8`
- 把 publisher 的 timer 从 `0.5` 改成 `0.2`
- 修改日志输出，让它更容易读

修改后在 Ubuntu VM 中重新执行：

```bash
cd ~/robotics-learning-log/week02_ros2_basics/ros2_ws
source /opt/ros/humble/setup.bash
colcon build --symlink-install
source install/setup.bash
ros2 launch fake_sensor_pkg sensor_demo.launch.py
```

记录修改前后有什么差异。

运行对比发现：

- publisher 的 timer 从 `0.5` 改成 `0.2` 后，发布频率变快。
- warning threshold 从 `1.0` 改成 `0.8` 后，只有距离小于 `0.8m` 时才打印 `WARNING`。
- 验证完成后，我把代码恢复回默认值，避免后续 Day 07 / Week 2 review 时默认行为和 README 不一致。

## 3. 记中文笔记（10 分钟）

- 今天改了哪一行？

今天做了两个实验性小改动：

1. 把 publisher 的 timer 从 `0.5` 改成 `0.2`，让发布频率变快。
2. 把 warning threshold 从 `1.0` 改成 `0.8`，让 warning 条件更严格。

验证完成后，代码已经恢复默认值：

```text
publisher timer: 0.5
WARNING_DISTANCE_M: 1.0
```

- 为什么要重新 build / source？

因为 ROS2 workspace 里的代码改动后，需要重新构建，让改动进入 `install/` 目录。

```bash
colcon build --symlink-install
```

负责重新构建 workspace。

```bash
source install/setup.bash
```

负责让当前终端加载这个 workspace 的环境。这样后面运行 `ros2 launch` 或 `ros2 run` 时，使用的就是最新构建后的 package。

- 修改后的现象是否符合预期？

符合预期。

- publish rate 变快：从每 `0.5s` 发布一次变成每 `0.2s` 发布一次。
- warning threshold 变小：从小于 `1.0m` warning 变成小于 `0.8m` warning。

- 遇到的报错和解决方式是什么？
暂时没有遇到报错。如果遇到会先根据报错信息排查可能错误的代码。

## 4. English Summary + Key Terms（10 分钟）

## English Summary

Today I modified the ROS2 fake sensor demo and tested the behavior in the Ubuntu VM.

I changed the publisher timer from `0.5` seconds to `0.2` seconds, so the publish rate became faster.

I also tested a smaller warning threshold and confirmed that a node only prints `WARNING` when its own condition is met.

I learned that the warning threshold is not sent inside the `/sensor/distance` message; only the distance value is sent.

After testing, I restored the code to the default values so the project behavior stays consistent with the README.

| English | 中文 |
|---------|------|
| warning threshold | 警告阈值 |
| publish rate | 发布频率 |
| rebuild | 重新构建 |
| iteration | 迭代 |
| debug | 调试 |
| runtime behavior | 运行时行为 |
| restore default | 恢复默认值 |
| parameter change | 参数修改 |

## 60-second Speaking Draft

Today I modified the ROS2 fake sensor demo and tested the result.

I changed one small requirement, rebuilt the workspace, and ran the launch file again.

This helped me understand the normal robotics development loop: edit code, build, source, run, and verify.

I also learned that small parameter changes can change the runtime behavior of a ROS2 node.

## 完成标准

- [x] 完成一个小改动
- [x] 重新 build 成功
- [x] 运行后观察到改动效果
- [x] 本日志已填写

## Git Commit

- Commit message：learn week02/day06
- Pushed to GitHub：Yes
