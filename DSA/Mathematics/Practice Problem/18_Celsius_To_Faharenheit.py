"""
Problem: Convert Celsius To Fahrenheit
Difficulty: Basic

Question:
Given a temperature in Celsius C, convert it to Fahrenheit.

Formula:

F = (9/5 × C) + 32

Examples:

Input: C = 32
Output: 89.6

Explanation:
(32 × 1.8) + 32 = 89.6

Input: C = 50
Output: 122

Explanation:
(50 × 1.8) + 32 = 122

Constraints:
1 ≤ C ≤ 10^4

Approach:
Use the Celsius to Fahrenheit conversion formula:

F = (9/5 × C) + 32

Time Complexity: O(1)
Space Complexity: O(1)
"""


def c_to_f(C):
    return (C * 1.8) + 32


if __name__ == "__main__":
    C = 32
    print(c_to_f(C))