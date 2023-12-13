import random
import string
import sys
import time


def matrix_frames(word_length: int, chars: str, n: int = 4,
                  sleep: float = 0.1) -> str:
    prefix = ''
    for i in range(word_length):
        k = word_length - len(prefix)
        for frame in range(n):
            sys.stdout.write(f'\r{prefix}' + ''.join(random.choices(chars, k=k)))
            time.sleep(sleep)
        prefix += random.choice(chars)
    return prefix


if __name__ == "__main__":
    matrix_frames(int(sys.argv[1]) if len(sys.argv) > 1 else 10,
                  string.hexdigits)

