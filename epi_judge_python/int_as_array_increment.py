from test_framework import generic_test


def plus_one(A):
    carry = 1
    for i in reversed(range(len(A))):
        if A[i] + carry == 10:
            A[i], carry = 0, 1
            if i == 0:
                A[i] = 1
                A.append(0)
        else:
            A[i] += 1
            return A
    return A


if __name__ == '__main__':
    plus_one([9, 9, 9, 9])
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
