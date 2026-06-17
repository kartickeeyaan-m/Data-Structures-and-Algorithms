"""
Problem: Modular Inverse
Difficulty: Easy

Question:
Given two integers n and m, return the smallest positive
integer x such that:

(n × x) % m = 1

If no such integer exists, return -1.

Examples:

Input: n = 3, m = 11
Output: 4

Explanation:
(3 × 4) % 11 = 1

Input: n = 10, m = 17
Output: 12

Explanation:
(10 × 12) % 17 = 1

Constraints:
1 ≤ n ≤ 10^4
1 ≤ m ≤ 10^5

Approach:
Use the Extended Euclidean Algorithm.

A modular inverse exists only when:

gcd(n, m) = 1

The Extended Euclidean Algorithm finds integers
x and y such that:

n*x + m*y = gcd(n, m)

If gcd(n, m) = 1, then x is the modular inverse.

Time Complexity: O(log m)
Space Complexity: O(log m)
"""

'''
def modInverse(n, m):

    for x in range(1, m):
        if ((n % m) * (x % m)) % m == 1:
            return x

    return -1
'''


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return gcd, x, y


def mod_inverse(n, m):
    gcd, x, _ = extended_gcd(n, m)

    if gcd != 1:
        return -1

    return (x % m + m) % m


if __name__ == "__main__":
    n = 3
    m = 11

    print(mod_inverse(n, m))