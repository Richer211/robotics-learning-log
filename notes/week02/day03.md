# Week 2 Day 03 - Read ROS2 Publisher / Subscriber Code

> 状态：**进行中** — 已阅读 publisher / subscriber 代码，已修正核心概念；`WARNING_DISTANCE_M = 0.8` 还需要同步到 VM 后重新 build/run 验证。

## Today's Goal

- [x] 读懂 `distance_publisher.py`
- [x] 读懂 `distance_subscriber.py`
- [x] 理解 `rclpy`、`Node`、`Range`、timer、callback`

## 1. 学（30 分钟）

重点阅读：

- `week02_ros2_basics/ros2_ws/src/fake_sensor_pkg/fake_sensor_pkg/distance_publisher.py`
- `week02_ros2_basics/ros2_ws/src/fake_sensor_pkg/fake_sensor_pkg/distance_subscriber.py`

回答：

- `DistancePublisher(Node)` 为什么继承 `Node`？

因为 `DistancePublisher` 本身要成为一个 ROS2 node，也就是一个正在运行的 ROS2 功能模块。

继承 `Node` 之后，`DistancePublisher` 才能使用 ROS2 node 的能力，比如：

- 创建 publisher
- 创建 timer
- 获取 logger
- 获取当前 ROS2 时间

简单理解：

```text
DistancePublisher 继承 Node
= 让这个 Python class 变成一个真正的 ROS2 节点
```

- `create_publisher(Range, '/sensor/distance', 10)` 三个参数分别是什么？

1. `Range`：消息类型，表示这个 topic 发送的是 `sensor_msgs/Range` 距离消息。
2. `/sensor/distance`：topic 名字，也就是数据频道。
3. `10`：QoS queue depth，可以先理解成消息队列缓存大小，不是打印帧数。

这行代码的意思是：

```text
创建一个 publisher，让它往 /sensor/distance 这个 topic 发布 Range 类型的消息。
```

- `create_timer(0.5, self.publish_reading)` 表示什么？

表示创建一个 timer，每 `0.5` 秒自动调用一次 `self.publish_reading`。

也就是说，publisher 不是只发布一次，而是每 0.5 秒生成并发布一条新的距离消息。

- subscriber 的 `callback(self, msg)` 什么时候被调用？

当 subscriber 从 `/sensor/distance` 收到一条新的 `Range` message 时，ROS2 会自动调用 `callback(self, msg)`。

这里不是“传感器移动每一帧时”直接调用，而是：

```text
publisher 发布消息
→ 消息进入 /sensor/distance
→ subscriber 收到消息
→ ROS2 自动调用 callback
```

- `rclpy.spin(node)` 为什么不能省略？

`rclpy.spin(node)` 会让 node 持续运行，并持续处理 ROS2 事件。

对 publisher 来说，它让 timer 可以不断触发 `publish_reading()`。

对 subscriber 来说，它让 node 可以不断等待消息，并在收到消息时触发 `callback()`。

如果没有 `rclpy.spin(node)`，程序很快就会结束，timer 不会持续触发，subscriber 也收不到消息。

## 2. 练（30 分钟）

在 VM 中重新运行 Day 02 demo，并边运行边看代码：

```bash
cd ~/robotics-learning-log/week02_ros2_basics/ros2_ws
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 launch fake_sensor_pkg sensor_demo.launch.py
```

观察输出后按 `Ctrl+C` 停止。

可选：把 subscriber 的 warning 阈值从 `1.0` 改成 `0.8`，重新 build/run，对比 WARNING 次数。

## 3. 记中文笔记（10 分钟）

- publisher 的主流程

1. `rclpy.init(args=args)`：初始化 ROS2 Python 环境。
2. `node = DistancePublisher()`：创建 publisher 节点对象。
3. `rclpy.spin(node)`：让 publisher 节点持续运行，timer 每 0.5 秒触发一次 `publish_reading()`。
4. `publish_reading()` 创建 `Range` message，填入距离信息，并发布到 `/sensor/distance`。
5. 如果出现 `KeyboardInterrupt`，也就是按下 `Ctrl+C`，程序会进入停止流程。
6. `node.destroy_node()`：销毁节点。
7. `rclpy.shutdown()`：关闭 ROS2 Python 环境。

- subscriber 的主流程

1. `rclpy.init(args=args)`：初始化 ROS2 Python 环境。
2. `node = DistanceSubscriber()`：创建 subscriber 节点对象。
3. `create_subscription(...)`：订阅 `/sensor/distance` topic。
4. `rclpy.spin(node)`：让 subscriber 持续运行，等待 topic 上的新消息。
5. 每收到一条新的 `Range` message，ROS2 就自动调用 `callback(self, msg)`。
6. `callback()` 读取 `msg.range`，如果距离小于 `WARNING_DISTANCE_M`，就打印 `WARNING`。
7. 停止程序后，销毁节点并关闭 ROS2 Python 环境。

- `Range` message 里你认识的字段

1. `header`：消息头，包含时间戳和 `frame_id`
2. `radiation_type`：传感器类型
3. `field_of_view`：视野角度
4. `min_range`：最小测距范围
5. `max_range`：最大测距范围
6. `range`：当前这一次测到的距离值

- 目前最不懂的一行代码
`self.publisher_ = self.create_publisher(Range, '/sensor/distance', 10)`，
`self.subscription = self.create_subscription(Range,'/sensor/distance',self.callback,10,)`

现在的最小理解：

```text
create_publisher(...)
= 创建一个发送方，往某个 topic 发某种类型的 message

create_subscription(...)
= 创建一个接收方，从某个 topic 接收某种类型的 message，并在收到消息时调用 callback
```

参数对照：

| 代码 | 含义 |
|------|------|
| `Range` | message 类型 |
| `/sensor/distance` | topic 名字 |
| `self.callback` | 收到消息后自动调用的函数 |
| `10` | QoS queue depth，先理解为消息缓存队列大小 |

### 关于 `WARNING_DISTANCE_M = 0.8`

我已经在本地代码里把 subscriber 的 warning 阈值从 `1.0` 改成了 `0.8`。

但因为 VM 里运行的是另一份从 GitHub clone 下来的仓库，所以这个改动还没有自动进入 VM。

后续需要：

```text
macOS 本地 commit / push
→ VM 里 git pull
→ VM 里 colcon build --symlink-install
→ source install/setup.bash
→ 重新运行测试
```

这样才能确认 subscriber 在距离小于 `0.8m` 时才打印 `WARNING`。

## 4. English Summary + Key Terms（10 分钟）

| English | 中文 |
|---------|------|
| rclpy | ROS2 Python 客户端库 |
| callback | 回调函数 |
| timer | 定时器 |
| Range message | 距离范围消息 |
| spin | 让节点持续处理事件 |

## 60-second Speaking Draft

Today I read the ROS2 publisher and subscriber code.

The publisher creates a `Range` message and publishes it every 0.5 seconds.

The subscriber receives the message in a callback function.

I learned that `rclpy.spin()` keeps a ROS2 node alive so it can process timers and messages.

## 完成标准

- [x] 能解释 publisher 代码主流程
- [x] 能解释 subscriber 代码主流程
- [x] 能说出 `callback` 什么时候触发
- [x] 本日志已填写

## Git Commit

- Commit message：
- Pushed to GitHub：No
