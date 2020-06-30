from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n):
    primes = []
    if n >= 2:
        primes.append(2)
    for i in range(3, n, 2):
        is_prime = True
        for k in range(3, int(i**.5)):
            if i % k == 0:
                is_prime = False
                continue
        if is_prime:
            primes.append(i)

    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("prime_sieve.py", "prime_sieve.tsv",
                                       generate_primes))
