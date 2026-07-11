# Week 2 Day 05 - ROS2 Bag Record / Playback

> 状态：**已完成** — 已成功录制并回放 `/sensor/distance` topic 数据，subscriber 能收到回放数据。

## Today's Goal

- [x] 使用 `ros2 bag record` 录制 `/sensor/distance`
- [x] 使用 `ros2 bag play` 回放数据
- [x] 理解 rosbag 和机器人数据记录的关系

## 1. 学（30 分钟）

阅读 `[../../week02_ros2_basics/README.md](../../week02_ros2_basics/README.md)` 的 Rosbag 部分。

回答：

- rosbag 是什么？

rosbag 是 ROS2 用来录制和回放 topic message 的工具。

它记录的不是 publisher 程序本身，而是 topic 上传输的数据。

本项目里录制的是：

```text
/sensor/distance
```

也就是 fake distance sensor 发布出来的 `Range` message。

- 为什么机器人开发需要录制传感器数据？

机器人开发需要录制传感器数据，是因为真实机器人运行一次成本高，而且真实环境不一定能完全重复。

把传感器数据录下来之后，就可以离线回放同一段数据，反复调试 perception、control、planning 等算法。

比如真实机器人在某个路面、光照、噪音、障碍物距离条件下出现问题，可以把当时的数据录下来，之后不用重新跑机器人，也能在电脑上重复分析。

- `record` 和 `play` 分别做什么？
- `record`：把某个 topic 上正在传输的 message 录制成 bag 文件。
- `play`：把 bag 文件里的 message 按时间顺序重新发布出来，像重新播放当时的数据。

简单理解：

```text
record = 录下来
play   = 重新播出来
```

- 为什么 rosbag 对调试 perception / control 很重要？

rosbag 对 perception / control 很重要，因为它可以把真实运行时的传感器数据保存下来。

perception 算法可以用同一段数据反复测试检测效果；control 算法也可以根据记录的数据分析机器人在某些情况下的行为是否合理。

这让调试不再完全依赖“每次都重新跑真实机器人”。

## 2. 练（30 分钟）

终端 1：启动 publisher / subscriber：

```bash
cd ~/robotics-learning-log/week02_ros2_basics/ros2_ws
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 launch fake_sensor_pkg sensor_demo.launch.py
```

终端 2：录制 topic：

```bash
cd ~/robotics-learning-log/week02_ros2_basics/ros2_ws
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 bag record /sensor/distance -o bags/week02_distance
```

```bash
ichard@ubuntu-ros2:~/robotics-learning-log/week02_ros2_basics/ros2_ws$ ros2 bag record /sensor/distance -o bags/week02_distance
[INFO] [1783739316.607509693] [rosbag2_recorder]: Press SPACE for pausing/resuming
[INFO] [1783739316.613072118] [rosbag2_storage]: Opened database 'bags/week02_distance/week02_distance_0.db3' for READ_WRITE.
[INFO] [1783739316.616432833] [rosbag2_recorder]: Listening for topics...
[INFO] [1783739316.616549421] [rosbag2_recorder]: Event publisher thread: Starting
[INFO] [1783739316.624992542] [rosbag2_recorder]: Subscribed to topic '/sensor/distance'
[INFO] [1783739316.625085671] [rosbag2_recorder]: Recording...
[INFO] [1783739316.625281137] [rosbag2_recorder]: All requested topics are subscribed. Stopping discovery...
[INFO] [1783739349.451726793] [rosbag2_cpp]: Writing remaining messages from cache to the bag. It may take a while
[INFO] [1783739349.452893169] [rosbag2_recorder]: Event publisher thread: Exiting
```

按 `Ctrl+C` 停止录制后，回放：

```bash
ros2 bag play bags/week02_distance
```

```bash
[INFO] [1783739392.191771719] [rosbag2_storage]: Opened database 'bags/week02_distance/week02_distance_0.db3' for READ_ONLY.
[INFO] [1783739392.191860097] [rosbag2_player]: Set rate to 1
[INFO] [1783739392.197013440] [rosbag2_player]: Adding keyboard callbacks.
[INFO] [1783739392.197080026] [rosbag2_player]: Press SPACE for Pause/Resume
[INFO] [1783739392.197097485] [rosbag2_player]: Press CURSOR_RIGHT for Play Next Message
[INFO] [1783739392.197115444] [rosbag2_player]: Press CURSOR_UP for Increase Rate 10%
[INFO] [1783739392.197131694] [rosbag2_player]: Press CURSOR_DOWN for Decrease Rate 10%
[INFO] [1783739392.197751007] [rosbag2_storage]: Opened database 'bags/week02_distance/week02_distance_0.db3' for READ_ONLY.
```



## 3. 记中文笔记（10 分钟）

- rosbag 生成了哪些文件？

生成了一个 bag 文件夹：

```text
bags/week02_distance/
```

里面主要包括：

```text
bags/week02_distance/week02_distance_0.db3
bags/week02_distance/metadata.yaml
```

其中：

- `week02_distance_0.db3`：保存录制下来的 topic 数据。
- `metadata.yaml`：保存 bag 的元信息，比如录了哪些 topic、消息类型、时长等。

注意：`rosbag2_cpp` 不是生成的文件，它是终端日志里显示的 ROS2 rosbag 模块名。

- 回放时 subscriber 能否收到数据？
可以收到数据如下：

```bash
[distance_subscriber-2] [INFO] [1783739808.574323669] [distance_subscriber]: [1251] distance=1.41 m
[distance_publisher-1] [WARN] [1783739809.072701794] [distance_publisher]: Frame 1186: close obstacle at 0.94 m
[distance_subscriber-2] [INFO] [1783739809.073154552] [distance_subscriber]: [1252] distance=0.94 m
```

说明：subscriber 可以收到 rosbag 回放出来的 `/sensor/distance` 数据。

如果 publisher 还在运行，subscriber 可能会同时收到 publisher 的实时数据和 `ros2 bag play` 回放的数据。

为了更清楚地观察回放，可以先停止 publisher，只保留 subscriber，然后运行：

```bash
ros2 bag play bags/week02_distance
```

- 录制/回放对真实机器人调试有什么帮助？

录制/回放可以帮助真实机器人调试传感器数据、速度、角度、障碍物距离等运行信息。

例如机器人在噪音、复杂路面、光照变化、障碍物靠近等情况下出现问题时，可以把当时的数据录下来，之后反复回放和分析。

这样可以降低调试成本，也可以让 perception / control 算法在同一段数据上反复测试。

## 4. English Summary + Key Terms（10 分钟）



## English Summary

Today I practiced recording and playing back ROS2 topic data with rosbag.

I recorded the `/sensor/distance` topic while the fake distance sensor demo was running.

I learned that rosbag records topic messages, not the publisher program itself.

After recording, I played the bag file back and confirmed that the subscriber could receive the replayed data.

This is useful in robotics because engineers can debug perception and control algorithms without running the real robot every time.


| English      | 中文      |
| ------------ | ------- |
| rosbag       | ROS 数据包 |
| record       | 录制      |
| playback     | 回放      |
| telemetry    | 遥测/运行数据 |
| data logging | 数据记录    |
| bag file     | 数据包文件   |
| metadata     | 元信息     |
| replay       | 重新播放    |




## 60-second Speaking Draft

Today I practiced recording and playing back ROS2 topic data with rosbag.

I recorded the `/sensor/distance` topic while the fake sensor publisher was running.

Then I played the bag file back to reproduce the same sensor data.

This is useful in robotics because we can debug software without running the real robot every time.

## 完成标准

- [x] 成功 `ros2 bag record`
- [x] 成功 `ros2 bag play`
- [x] 能解释 rosbag 的用途
- [x] 本日志已填写



## Git Commit

- Commit message：learn day05
- Pushed to GitHub：Yes

