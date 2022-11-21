#!/usr/bin/env python

from copy import copy


def f(n: int) -> list[list[int]]:
    if n == 0:
        return []
    if n == 1:
        return [[1]]

    res = f(n - 1)
    res.append(copy(res[-1]))
    res[-1].append(n)

    return res


def main():
    for i in range(5):
        print(f"f({i})={f(i)}")


if __name__ == "__main__":
    main()
