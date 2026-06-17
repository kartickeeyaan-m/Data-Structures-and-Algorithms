"""
Problem: 3 Divisors
Difficulty: Medium

Question:
Given a number n, determine how many numbers less than
or equal to n have exactly 3 divisors.

Examples:

Input: n = 6
Output: 1

Explanation:
4 has exactly 3 divisors:
1, 2, 4

Input: n = 10
Output: 2

Explanation:
4 and 9 have exactly 3 divisors.

Constraints:
1 ≤ n ≤ 10^9

Approach:
A number has exactly 3 divisors if and only if it is
the square of a prime number.

Therefore:
1. Find all prime numbers ≤ √n using Sieve of Eratosthenes.
2. Count those primes.

Time Complexity: O(√n log log √n)
Space Complexity: O(√n)
"""

from math import isqrt


def exactly_3_divisors(n):
    limit = isqrt(n)

    prime = [True] * (limit + 1)

    if limit >= 0:
        prime[0] = False

    if limit >= 1:
        prime[1] = False

    p = 2

    while p * p <= limit:
        if prime[p]:
            for multiple in range(p * p, limit + 1, p):
                prime[multiple] = False

        p += 1

    count = 0

    for i in range(2, limit + 1):
        if prime[i]:
            count += 1

    return count


if __name__ == "__main__":
    n = 10
    print(exactly_3_divisors(n))