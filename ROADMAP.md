# Robotics Learning Roadmap

## Positioning

**CS background → Robotics Software, Computer Vision, ROS2, Simulation, Physical AI.**

## Job Priority (phase 1)

1. **Robotics Software Engineer / ROS2** — primary target
2. **Robotics Perception Engineer** — CV-aligned
3. **Robotics Simulation Engineer** — Gazebo / Isaac path
4. **Field Robotics / Deployment** — later integration focus

## Skill Stack

### Must have (now)

Python, C++ basics, Linux, Git, Docker basics, ROS2, OpenCV, PyTorch basics, camera calibration concepts, detection / segmentation basics, kinematics / localization / planning / control concepts.

### 3–6 months

Gazebo / Isaac Sim, depth / point cloud, sensor fusion, rosbag / telemetry, ONNX / TensorRT basics, FPS / latency profiling.

### 6–12 months

VLA models, manipulation, RL, CUDA depth — after core demos ship.

## Monthly Milestones

| When | Goal |
|------|------|
| **Month 1** | ROS2 basics + OpenCV/YOLO demo + ROS2 vision integration |
| **Month 2–4** | Main project: `projects/perception_sim` (perception + ROS2 + simulation) |
| **Month 5–6** | One side project (edge deploy / synthetic data / field debugging) |
| **Month 6** | Resume-ready portfolio, start applying junior robotics roles |

## Repo Timeline

| Folder | Week | Deliverable |
|--------|------|-------------|
| `python_practice/`, `cpp_practice/` | 1 | Fake sensor demos (class-based) |
| `week02_ros2_basics/` | 2 | Pub/sub, launch, rosbag, RViz |
| `week03_vision_demo/` | 3 | Video object detection + FPS |
| `week04_ros2_vision/` | 4 | Image topic → detection → viz + latency |
| `projects/perception_sim/` | 2–4 mo | Full perception + sim system |

## Hard Rules

1. **Every day**: code + run + modify + log + commit.
2. **AI usage**: explain → rewrite without AI → change requirements yourself.
3. **Video**: max 30–45 min/day; always follow with code.
4. **No marathon courses** — learn from the current task only.
5. **Ship runnable demos** — recruiters care about reproducible projects, not certificates.

## Daily Check

> Did I write code, run it, change it, and record what happened?

If yes → valid day. If only videos / bookmarks → not progress.
