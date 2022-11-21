#!/usr/bin/env python

import itertools
from typing import Iterator


def fibo() -> Iterator[int]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def main():
    even_fibo_numbers = (x for x in fibo() if x % 2 == 0)
    print(sum(itertools.islice(even_fibo_numbers, 100)))


if __name__ == "__main__":
    main()
