from test_framework import generic_test


def is_palindrome_number(x):
    if x <= 0:
        return x == 0
    reverse_digt = 0
    x_for_rev = x
    while x_for_rev:
        reverse_digt = reverse_digt * 10 + x_for_rev % 10
        x_for_rev //= 10
    return x == reverse_digt


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_number_palindromic.py",
                                       "is_number_palindromic.tsv",
                                       is_palindrome_number))
