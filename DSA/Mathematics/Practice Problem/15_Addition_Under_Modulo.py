"""
Problem: Addition Under Modulo
Difficulty: Basic

Question:
Given three integers a, b, and M, compute:

(a + b) mod M

Modular operation returns the remainder when divided by M.

Examples:

Input: a = 10, b = 20, M = 3
Output: 0

Explanation:
(10 + 20) mod 3 = 0

Input: a = 100, b = 13, M = 107
Output: 6

Explanation:
(100 + 13) mod 107 = 6

Constraints:
1 ≤ a, b, M ≤ 10^9

Approach:
Compute the sum of a and b, then take modulo M.

Formula:
(a + b) % M

Time Complexity: O(1)
Space Complexity: O(1)
"""


def sum_under_modulo(a, b, M):
    return (a + b) % M


if __name__ == "__main__":
    a = 10
    b = 20
    M = 3

    print(sum_under_modulo(a, b, M))