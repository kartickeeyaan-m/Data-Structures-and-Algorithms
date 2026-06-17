"""
Problem: LCM of Two Numbers
Difficulty: Easy

Question:
Given two positive integers a and b, compute and return their
Least Common Multiple (LCM).

The LCM of two integers is the smallest positive integer
that is divisible by both numbers.

Examples:

Input: a = 12, b = 18
Output: 36

Input: a = 5, b = 11
Output: 55

Constraints:
1 ≤ a, b ≤ 10^4

Approach:
Use the relation:

LCM(a, b) = (a * b) / GCD(a, b)

Compute GCD using Euclid's Algorithm and then apply the formula.

Time Complexity: O(log(min(a, b)))
Space Complexity: O(1)
"""


def gcd(a, b):
    while b:
        a, b = b, a % b

    return a


def lcm(a, b):
    return a * b // gcd(a, b)


if __name__ == "__main__":
    a = 12
    b = 18

    print(lcm(a, b))