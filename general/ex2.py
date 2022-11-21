#!/usr/bin/env python


def skip_first(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return []

    first = arr[0]
    for i in range(1, len(arr)):
        if first != arr[i]:
            break
    # The loop must have iterated at least once, i is bound
    return arr[i:]  # type: ignore


def solution(arr: list[int], other: list[int]) -> list[int]:
    res = []
    while True:
        if not arr or not other:
            break
        a = arr[0]
        b = other[0]
        if a == b:
            res.append(a)
        if a <= b:
            arr = skip_first(arr)
        if b <= a:
            other = skip_first(other)
    return res


def pythonic_solution(arr: list[int], other: list[int]) -> list[int]:
    return list(set(arr) & set(other))


if __name__ == "__main__":
    arr1 = [0, 1, 2, 3, 4, 5, 5, 5, 6, 7]
    arr2 = [0, 0, 3, 3, 3, 5, 6, 6, 7, 8]
    print(solution(arr1, arr2))
    print(pythonic_solution(arr1, arr2))
