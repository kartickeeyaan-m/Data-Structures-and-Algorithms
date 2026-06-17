"""
Problem: Sieve of Eratosthenes
Difficulty: Medium

Question:
Given a positive integer n, calculate and return all primes
less than or equal to n using the Sieve of Eratosthenes algorithm.

Examples:

Input: n = 10
Output: [2, 3, 5, 7]

Input: n = 35
Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

Constraints:
1 ≤ n ≤ 10^4

Approach:
1. Assume all numbers are prime.
2. Start from 2.
3. Mark all multiples of each prime as non-prime.
4. The remaining unmarked numbers are primes.

Time Complexity: O(n log log n)
Space Complexity: O(n)
"""


def sieve(n):
    is_prime = [True] * (n + 1)

    if n >= 0:
        is_prime[0] = False

    if n >= 1:
        is_prime[1] = False

    p = 2

    while p * p <= n:
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False

        p += 1

    primes = []

    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)

    return primes


if __name__ == "__main__":
    n = 10
    print(sieve(n))