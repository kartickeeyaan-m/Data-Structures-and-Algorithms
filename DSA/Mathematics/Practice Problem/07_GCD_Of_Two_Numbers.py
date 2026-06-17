"""
Problem: GCD of Two Numbers
Difficulty: Basic

Question:
Given two positive integers a and b, find the GCD of a and b.

Note:
Do not use the inbuilt gcd function.

Examples:

Input: a = 20, b = 28
Output: 4

Input: a = 60, b = 36
Output: 12

Constraints:
1 ≤ a, b ≤ 10^9

Approach:
Use Euclid's Algorithm.

Repeatedly replace:
(a, b) -> (b, a % b)

When b becomes 0, a is the GCD.

Time Complexity: O(log(min(a, b)))
Space Complexity: O(1)
"""


def gcd(a, b):
    while b > 0:
        a, b = b, a % b

    return a


if __name__ == "__main__":
    a = 20
    b = 28

    print(gcd(a, b))