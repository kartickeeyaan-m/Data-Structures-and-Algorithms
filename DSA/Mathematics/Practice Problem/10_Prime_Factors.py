"""
Problem: All Prime Factors in Any Order
Difficulty: Medium

Question:
Given a positive integer n, return its prime factors in any order.

A prime number is a natural number greater than 1
that has no positive divisors other than 1 and itself.

Examples:

Input: n = 18
Output: [2, 3, 3]

Explanation:
18 = 2 × 3 × 3

Input: n = 25
Output: [5, 5]

Explanation:
25 = 5 × 5

Constraints:
1 ≤ n ≤ 10^9

Approach:
1. Extract all factors of 2.
2. Check only odd divisors from 3 onwards.
3. Continue dividing while the factor exists.
4. If n > 1 at the end, it is also a prime factor.

Time Complexity: O(√n)
Space Complexity: O(k)
where k is the number of prime factors.
"""


def prime_factors(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n //= 2

    i = 3

    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i

        i += 2

    if n > 1:
        factors.append(n)

    return factors


if __name__ == "__main__":
    n = 18
    print(prime_factors(n))