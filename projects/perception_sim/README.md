# Perception + Simulation (Main Project)

**Status**: Planned — starts from Week 4 `ros2_vision` integration.

## Goal

A ROS2-based robotics perception and simulation system demonstrating:

1. **Perception** — detection, segmentation, visualization
2. **ROS2 Integration** — camera, perception, decision nodes, launch, rosbag
3. **Simulation** — Gazebo or Isaac Sim validation
4. **Sensor Fusion** — camera + depth (phase 2)
5. **Telemetry** — FPS, latency, dropped frames, logs

## Milestones

| Phase | Target | Source |
|-------|--------|--------|
| v0.1 | Video → detect → ROS2 topics | `week04_ros2_vision/` |
| v0.2 | Gazebo mobile robot + camera | Month 2 |
| v0.3 | Simple navigate / approach target | Month 3 |
| v1.0 | Demo video + reproducible README | Month 4 |

## Folder layout (future)

```
projects/perception_sim/
├── ros2_ws/
│   └── src/
│       ├── perception/      # from week04
│       ├── simulation/      # Gazebo worlds
│       └── telemetry/       # metrics dashboard
├── docs/
└── README.md
```

Start by copying and extending `week04_ros2_vision/ros2_ws/src/ros2_vision_pkg` when Month 2 begins.
