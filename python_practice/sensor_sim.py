import argparse
import random
import time
from pathlib import Path


class FakeSensor:
    """Simulates a distance sensor with optional temperature reading."""

    WARNING_DISTANCE_M = 1.0

    def __init__(self, min_distance: float = 0.1, max_distance: float = 5.0):
        self.min_distance = min_distance
        self.max_distance = max_distance

    def read_distance(self) -> float:
        return random.uniform(self.min_distance, self.max_distance)

    def read_temperature(self) -> float:
        return random.uniform(18.0, 35.0)

    def is_warning(self, distance: float) -> bool:
        return distance < self.WARNING_DISTANCE_M


def format_reading(frame: int, distance: float, temperature: float, warning: bool) -> str:
    status = "WARNING: obstacle close" if warning else "OK"
    return (
        f"Frame {frame}: distance={distance:.2f} m, "
        f"temp={temperature:.1f} C, status={status}"
    )


def main():
    parser = argparse.ArgumentParser(description="Fake distance + temperature sensor simulation")
    parser.add_argument("--frames", type=int, default=10, help="Number of readings to print")
    parser.add_argument("--interval", type=float, default=0.5, help="Seconds between readings")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("sensor_log.txt"),
        help="Path to save readings",
    )
    args = parser.parse_args()

    sensor = FakeSensor()
    args.output.parent.mkdir(parents=True, exist_ok=True)

    print("Starting sensor simulation...")
    lines = []

    for frame in range(args.frames):
        distance = sensor.read_distance()
        temperature = sensor.read_temperature()
        warning = sensor.is_warning(distance)
        line = format_reading(frame, distance, temperature, warning)
        print(line)
        lines.append(line)
        time.sleep(args.interval)

    args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Saved {len(lines)} readings to {args.output}")


if __name__ == "__main__":
    main()
