from test_framework import generic_test


def parity(x):
    mask_size = 16
    bit_mask = 0xffff
    return PRECOMPUTED_PARITY[x >> 3 * mask_size] ^ PRECOMPUTED_PARITY[x >> 2 * mask_size] & bit_mask ^ PRECOMPUTED_PARITY[x >>]


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
