from test_framework import generic_test


def multiply(x, y):
    def add(a, b):
        while b:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a
    result = 0
    while y:
        if y & 1:
            result = add(result, x)
        x, y = x << 1, y >> 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("primitive_multiply.py",
                                       'primitive_multiply.tsv', multiply))
