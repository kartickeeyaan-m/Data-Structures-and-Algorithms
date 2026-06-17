"""
Problem: Modular Multiplication
Difficulty: Easy

Question:
Given three integers a, b, and M, perform modular multiplication
and return:

(a × b) % M

where % denotes the modulo operation.

Examples:

Input: a = 5, b = 3, M = 11
Output: 4

Explanation:
5 × 3 = 15
15 % 11 = 4

Input: a = 12, b = 15, M = 7
Output: 5

Explanation:
12 × 15 = 180
180 % 7 = 5

Constraints:
1 ≤ a, b ≤ 10^4
2 ≤ M ≤ 10^9

Approach:
Multiply a and b, then take modulo M.

Formula:
(a × b) % M

Time Complexity: O(1)
Space Complexity: O(1)
"""


def modmul(a, b, M):
    return (a * b) % M


if __name__ == "__main__":
    a = 5
    b = 3
    M = 11

    print(modmul(a, b, M))