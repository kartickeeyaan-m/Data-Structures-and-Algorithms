"""
Problem: Factorial
Difficult: Basic

Given a positive integer n, find the factorial of n.

Examples:
Input: 5
Output: 120

Input: 4
Output: 24

Constraints:
0 <= n <= 12

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def factorial(self, n: int) -> int:
        res = 1

        for i in range(2, n + 1):
            res *= i

        return res


def main():
    n = int(input("Enter a number: "))

    obj = Solution()

    print("Factorial:", obj.factorial(n))


if __name__ == "__main__":
    main()