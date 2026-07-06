# Development Environment

## Strategy

Hybrid setup: **macOS for daily coding**, **Ubuntu 22.04 VM for ROS2 / simulation**.

| Phase | Environment | Purpose |
|-------|-------------|---------|
| Week 1 | macOS native | Python, C++, CMake, Git |
| Week 2+ | Ubuntu 22.04 VM (UTM) | ROS2 Humble, RViz, Gazebo, rosbag |
| Optional | Docker (`osrf/ros:humble-desktop`) | Reproducible builds, CI |
| 6+ months | NVIDIA GPU + Linux | Isaac Sim (when needed) |

## Host Machine

- **OS**: macOS (darwin)
- **Editor**: VS Code / Cursor
- **Tools**: Python 3, CMake, Git, Docker (optional)

## Ubuntu VM (UTM)

### Install UTM + Ubuntu 22.04

1. Download [UTM](https://mac.getutm.app/) and [Ubuntu 22.04 Desktop ISO](https://ubuntu.com/download/desktop).
2. Create a new VM: **ARM64** (Apple Silicon) or **x86_64** (Intel Mac).
3. Recommended resources:
   - RAM: **8 GB** minimum
   - Disk: **40 GB** minimum
   - CPU: 4 cores if available

### ROS2 Humble (inside VM)

```bash
# Locale
sudo apt update && sudo apt install -y locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

# ROS2 apt source
sudo apt install -y software-properties-common
sudo add-apt-repository universe
sudo apt update && sudo apt install -y curl
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
  -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] \
  http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | \
  sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

# Install ROS2 Humble Desktop
sudo apt update
sudo apt install -y ros-humble-desktop ros-dev-tools

# Shell setup (add to ~/.bashrc)
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc

# Verify
ros2 doctor
```

### Workspace layout (VM)

```bash
mkdir -p ~/robotics-learning-log
cd ~/robotics-learning-log
git clone https://github.com/Richer211/robotics-learning-log.git .
# Or sync week02+ folders from this repo

cd week02_ros2_basics/ros2_ws
colcon build
source install/setup.bash
```

## Docker (optional, macOS)

```bash
docker run hello-world

# ROS2 Humble shell (headless; GUI needs extra X11 setup)
docker run -it --rm osrf/ros:humble-desktop bash
```

## Verification Checklist

- [ ] macOS: `python3 --version`, `cmake --version`, `git --version`
- [ ] VM: `lsb_release -a` shows Ubuntu 22.04
- [ ] VM: `ros2 doctor` passes
- [ ] VM: `colcon build` succeeds in `week02_ros2_basics/ros2_ws`
- [ ] Docker: `docker run hello-world` (optional)

## Notes

- Prefer **Ubuntu VM** over macOS-native ROS2 for RViz / Gazebo.
- Keep ROS2 projects under `week02_ros2_basics/` and `week04_ros2_vision/`; build inside the VM.
- Document versions here when you complete VM setup (UTM version, Ubuntu image date).
