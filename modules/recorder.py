import cv2
import os
import time
from datetime import datetime


class VideoRecorder:

    def __init__(self, fps=30, duration=10):

        self.fps = fps
        self.duration = duration

        self.recording = False
        self.start_time = 0

        self.writer = None
        self.filename = None

        os.makedirs("clips", exist_ok=True)

    def start_recording(self, frame):

        if self.recording:
            return

        height, width = frame.shape[:2]

        self.filename = datetime.now().strftime(
            "clips/incident_%Y%m%d_%H%M%S.mp4"
        )

        self.writer = cv2.VideoWriter(
            self.filename,
            cv2.VideoWriter_fourcc(*"mp4v"),
            self.fps,
            (width, height)
        )

        self.recording = True
        self.start_time = time.time()

        print("🎥 Recording started...")

    def update(self, frame):

        if not self.recording:
            return

        self.writer.write(frame)

        elapsed = time.time() - self.start_time

        if elapsed >= self.duration:

            self.writer.release()

            print(f"✅ Clip saved: {self.filename}")

            self.writer = None
            self.filename = None
            self.recording = False


recorder = VideoRecorder()