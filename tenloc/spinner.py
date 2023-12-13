import sys
import time


def spin(frames: list[str], pause: float = 0.2):
    for frame in frames:
        sys.stdout.write(f'\r{frame}')
        time.sleep(pause)

if __name__ == "__main__":
    while True:
        spin(['\\', '|', '/', '--'])
