import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def even_odd(A):
    even, odd = 0, len(A)-1
    while even < odd:
        if A[even] % 2 != 0 and A[odd] % 2 == 0:
            # swap
            A[odd], A[even] = A[even], A[odd]
            odd -= 1
            even += 1
            continue
        if A[even] % 2 == 0:
            even += 1
        if A[odd] % 2 != 0:
            odd -= 1

@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure("Even elements appear in odd part")
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure("Elements mismatch")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_array.py",
                                       'even_odd_array.tsv', even_odd_wrapper))
