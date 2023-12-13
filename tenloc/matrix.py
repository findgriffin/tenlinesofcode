import random
import string
import sys
import time


def matrix_frames(prefix: str, word_length: int, chars: str, n: int=4) -> str:
    k = word_length - len(prefix)
    for frame in range(n):
        sys.stdout.write(f'\r{prefix}' + ''.join(random.choices(chars, k=k)))
        time.sleep(0.1)
    return prefix + random.choice(chars)


if __name__ == "__main__":
    prefix = ''
    word_length = sys.argv[1] if len(sys.argv) > 1 else 10
    for i in range(word_length):
        prefix = matrix_frames(prefix, word_length, string.hexdigits)
