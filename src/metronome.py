import time


def metronome(delta: int = 2, testing: bool = False):
    previous = 0.0
    tested = False
    while True and not tested:
        now = time.time()
        if (now - previous) > delta:
            print('\a')
            previous = now
            if testing:
                tested = True
        time.sleep(delta/100)
