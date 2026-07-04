# Robotics Learning Log

This repository records my learning progress in **Robotics Software, ROS2, Computer Vision, and Physical AI**.

**Target roles**: Robotics Software Engineer, Robotics Perception Engineer, ROS2 / Simulation.

See [ROADMAP.md](ROADMAP.md) for milestones and [notes/environment.md](notes/environment.md) for dev setup.

## Repository Layout

| Path | Week | Description |
|------|------|-------------|
| `python_practice/` | 1 | Python fake sensor (class-based) |
| `cpp_practice/` | 1 | C++ fake sensor + CMake |
| `notes/` | ongoing | Daily logs, templates, environment docs |
| `week02_ros2_basics/` | 2 | ROS2 pub/sub, launch, rosbag |
| `week03_vision_demo/` | 3 | OpenCV + YOLO video detection + FPS |
| `week04_ros2_vision/` | 4 | ROS2 image → perception → metrics |
| `projects/perception_sim/` | 2–4 mo | Main project (scaffold) |

## Start Here

**每天只看这个文件 → [notes/CURRENT.md](notes/CURRENT.md)**

**英文同步学习**：每日 English Summary + Key Terms；词汇表 [notes/glossary/robotics-terms.md](notes/glossary/robotics-terms.md)；口语流程 [notes/speaking/README.md](notes/speaking/README.md)

## Progress

### Week 1 (in progress)

- Day 01 ✅: GitHub repo, Python + C++ fake sensor demos — [notes/day01.md](notes/day01.md)
- Day 02 ← **今天**: Linux + Git — [notes/day02.md](notes/day02.md)
- Day 03–07: 见 [notes/week1-schedule.md](notes/week1-schedule.md)

### Week 2–4 (代码已准备好，按周执行)

- Week 2: [week02_ros2_basics/README.md](week02_ros2_basics/README.md)（需 Ubuntu VM）
- Week 3: [week03_vision_demo/README.md](week03_vision_demo/README.md)
- Week 4: [week04_ros2_vision/README.md](week04_ros2_vision/README.md)

## Build & Run (Week 1)

### Python fake sensor

```bash
cd python_practice
python3 sensor_sim.py --frames 10 --interval 0.5
# Output log: sensor_log.txt (in current working directory)
```

### C++ fake sensor

```bash
cd cpp_practice/fake_sensor_cpp
mkdir -p build && cd build
cmake ..
make
./fake_sensor
# Output log: sensor_log.txt (run from build/ directory)
```

## ROS2 Projects (Ubuntu VM)

ROS2 Humble demos live under `week02_ros2_basics/` and `week04_ros2_vision/`. Build inside Ubuntu 22.04:

```bash
source /opt/ros/humble/setup.bash
cd week02_ros2_basics/ros2_ws && colcon build && source install/setup.bash
```

## Learning Logs

- Templates: [notes/templates/](notes/templates/)
- Daily logs: [notes/day01.md](notes/day01.md) … [notes/day07.md](notes/day07.md)

## Current Stage

**Day 02** — Linux + Git 练习。完整日程见 [notes/week1-schedule.md](notes/week1-schedule.md)。
