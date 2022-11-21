#!/usr/bin/env python

from typing import Iterator


def multiples_of(n: int, max: int) -> Iterator[int]:
    assert n > 0, f"n must be striclyt positive, got: {n}"
    i = 0
    while i < max:
        yield i
        i += n


def main():
    print(sum(multiples_of(3, 102030)))


if __name__ == "__main__":
    main()
