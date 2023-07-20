import time


def metronome(delta: int = 2):
    previous = 0
    while True:
        now = time.time()
        if (now - previous) > delta:
            print('\a')
            previous = now
        time.sleep(delta/100)