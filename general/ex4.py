#!/usr/bin/env python


def naive_solution(x: int) -> int:
    assert 0 <= x < 10, f"{x} is not a digit"
    xx = x * 10 + x
    xxx = xx * 10 + x
    xxxx = xxx * 10 + x
    return x + xx + xxx + xxxx


def solution(x: int) -> int:
    assert 0 <= x < 10, f"{x} is not a digit"
    return x * 1234


if __name__ == "__main__":
    for x in range(10):
        print(f"{naive_solution(x)} == {solution(x)}")
