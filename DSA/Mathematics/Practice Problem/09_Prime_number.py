"""
Problem: Prime Number
Difficulty: Easy

Question:
Given a number n, determine whether it is a prime number or not.

A prime number is a number greater than 1 that has no positive
divisors other than 1 and itself.

Examples:

Input: n = 7
Output: True

Input: n = 25
Output: False

Input: n = 1
Output: False

Constraints:
1 ≤ n ≤ 10^9

Approach:
1. Handle edge cases for n <= 1, 2, and 3.
2. Eliminate multiples of 2 and 3.
3. Check divisibility only for numbers of the form 6k ± 1.
4. Stop when i * i > n.

Time Complexity: O(√n)
Space Complexity: O(1)
"""


def is_prime(n):
    if n <= 1:
        return False

    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5

    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False

        i += 6

    return True


if __name__ == "__main__":
    n = 7
    print(is_prime(n))