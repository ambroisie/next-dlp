#!/usr/bin/env python


def solution(n: int) -> bool:
    if n < 0:
        n = -n

    while n:
        if n % 2 == 1:
            return False
        n //= 10

    return True


if __name__ == "__main__":
    print(solution(0))
    print(solution(1))
    print(solution(2468))
    print(solution(1468))
    print(solution(-2468))
    print(solution(-2469))
