import argparse
import random
import time
from pathlib import Path


class FakeSensor:
    """Simulates a distance sensor with optional temperature reading."""

    WARNING_DISTANCE_M = 0.8 # 警告距离:1米,表示距离传感器读取的距离小于1米时,表示有障碍物

    def __init__(self, min_distance: float = 0.1, max_distance: float = 5.0):
        self.min_distance = min_distance
        self.max_distance = max_distance

    def read_distance(self) -> float:
        return random.uniform(self.min_distance, self.max_distance) # 创建一个随机数,范围在0.1和5之间,表示距离传感器读取的距离

    def read_temperature(self) -> float:
        return random.uniform(18.0, 35.0) # 创建一个随机数,范围在18和35之间,表示温度传感器读取的温度

    def is_warning(self, distance: float) -> bool:
        return distance < self.WARNING_DISTANCE_M # 如果距离小于1米,则返回True,表示有障碍物


def format_reading(frame: int, distance: float, temperature: float, warning: bool) -> str:
    status = "WARNING: obstacle close" if warning else "OK" # 如果warning为True,则状态为"WARNING: obstacle close",否则为"OK"
    return (
        f"Frame {frame}: distance={distance:.2f} m, " # 距离:2位小数,单位米
        f"temp={temperature:.1f} C, status={status}" # 返回一个字符串,表示帧号,距离,温度和状态
    )


def main():
    parser = argparse.ArgumentParser(description="Fake distance + temperature sensor simulation") # 创建一个参数解析器,用于解析命令行参数
    parser.add_argument("--frames", type=int, default=10, help="Number of readings to print") # 帧数:10,表示读取10次
    parser.add_argument("--interval", type=float, default=0.5, help="Seconds between readings") # 间隔:0.5秒,表示每次读取间隔0.5秒
    parser.add_argument(
        "--output",
        type=Path, # 路径:sensor_log.txt,表示保存读取的距离和温度
        default=Path("sensor_log.txt"), # 默认路径:sensor_log.txt
        help="Path to save readings",
    )
    args = parser.parse_args() # 解析命令行参数

    sensor = FakeSensor() # 创建一个传感器对象
    args.output.parent.mkdir(parents=True, exist_ok=True) # 创建一个目录,用于保存读取的距离和温度

    print("Starting sensor simulation...") # 打印开始传感器模拟
    lines = [] # 创建一个列表,用于保存读取的距离和温度
    random.seed(42) # 设置随机种子,用于每次运行时生成相同的随机数
    for frame in range(args.frames): # 遍历帧数,表示读取10次
        distance = sensor.read_distance() # 读取距离
        temperature = sensor.read_temperature() # 读取温度
        warning = sensor.is_warning(distance) # 判断是否警告
        line = format_reading(frame, distance, temperature, warning) # 格式化读取的距离和温度
        print(line) # 打印读取的距离和温度
        lines.append(line) # 将读取的距离和温度添加到列表中
        time.sleep(args.interval) # 等待0.5秒

    args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Saved {len(lines)} readings to {args.output}")


if __name__ == "__main__":
    main()
