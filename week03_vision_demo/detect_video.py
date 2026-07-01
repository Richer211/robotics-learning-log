#!/usr/bin/env python3
"""Video object detection demo with FPS tracking."""

import argparse
import time
from pathlib import Path

import cv2


def parse_args():
  parser = argparse.ArgumentParser(description='Run YOLO object detection on a video file')
  parser.add_argument('--source', type=Path, required=True, help='Input video path or camera index (0)')
  parser.add_argument('--model', type=str, default='yolov8n.pt', help='Ultralytics model weights')
  parser.add_argument('--output', type=Path, default=Path('week03_vision_demo/output/annotated.mp4'))
  parser.add_argument('--conf', type=float, default=0.4, help='Confidence threshold')
  parser.add_argument('--max-frames', type=int, default=0, help='Limit frames (0 = all)')
  return parser.parse_args()


def open_capture(source: str | Path):
  if str(source).isdigit():
    return cv2.VideoCapture(int(source))
  return cv2.VideoCapture(str(source))


def main():
  args = parse_args()

  try:
    from ultralytics import YOLO
  except ImportError as exc:
    raise SystemExit('Install dependencies: pip install -r requirements.txt') from exc

  cap = open_capture(args.source)
  if not cap.isOpened():
    raise SystemExit(f'Cannot open video source: {args.source}')

  model = YOLO(args.model)
  args.output.parent.mkdir(parents=True, exist_ok=True)

  width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
  height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
  fps_in = cap.get(cv2.CAP_PROP_FPS) or 30.0
  writer = cv2.VideoWriter(
    str(args.output),
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps_in,
    (width, height),
  )

  frame_count = 0
  total_infer_ms = 0.0

  print(f'Running detection: source={args.source}, model={args.model}')

  while cap.isOpened():
    ok, frame = cap.read()
    if not ok:
      break

    start = time.perf_counter()
    results = model.predict(frame, conf=args.conf, verbose=False)
    infer_ms = (time.perf_counter() - start) * 1000.0
    total_infer_ms += infer_ms

    annotated = results[0].plot()
    writer.write(annotated)

    frame_count += 1
    if frame_count % 30 == 0:
      avg_ms = total_infer_ms / frame_count
      print(f'Frame {frame_count}: infer={infer_ms:.1f} ms, avg={avg_ms:.1f} ms, FPS={1000.0/avg_ms:.1f}')

    if args.max_frames and frame_count >= args.max_frames:
      break

  cap.release()
  writer.release()

  if frame_count == 0:
    raise SystemExit('No frames processed.')

  avg_ms = total_infer_ms / frame_count
  print('--- Summary ---')
  print(f'Frames: {frame_count}')
  print(f'Avg inference: {avg_ms:.2f} ms')
  print(f'Avg FPS: {1000.0 / avg_ms:.2f}')
  print(f'Output: {args.output}')


if __name__ == '__main__':
  main()
