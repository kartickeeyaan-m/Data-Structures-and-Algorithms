"""
Problem: Sum of Natural Numbers
Difficulty: Easy

Question:
Given an integer n, compute the sum of all natural numbers from 1 to n (inclusive).
If n is 0, the sum should be 0.

Examples:

Input: n = 6
Output: 21

Input: n = 4
Output: 10

Input: n = 0
Output: 0

Constraints:
0 ≤ n ≤ 10^4

Approach:
Use the mathematical formula:

Sum = n * (n + 1) / 2

This computes the answer in constant time.

Time Complexity: O(1)
Space Complexity: O(1)
"""


def sum_of_natural_numbers(n):
    return n * (n + 1) // 2


if __name__ == "__main__":
    n = 6
    print(sum_of_natural_numbers(n))