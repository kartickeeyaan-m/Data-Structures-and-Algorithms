"""
Problem: 50. Pow(x, n)
Difficulty: Medium

Question:
Implement pow(x, n), which calculates x raised to the power n.

Examples:

Input: x = 2.00000, n = 10
Output: 1024.00000

Input: x = 2.10000, n = 3
Output: 9.26100

Input: x = 2.00000, n = -2
Output: 0.25000

Constraints:
-100 < x < 100
-2^31 <= n <= 2^31 - 1

Approach:
Use Binary Exponentiation.

If n is odd:
    result *= x

Square x each step:
    x = x * x

Reduce exponent:
    n = n // 2

This reduces the exponent by half every iteration.

Time Complexity: O(log n)
Space Complexity: O(1)
"""
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            return 1 / self.myPow(x, -n)

        temp = self.myPow(x, n // 2)

        if n % 2 == 0:
            return temp * temp
        else:
            return x * temp * temp
'''
def my_pow(x, n):
    if n < 0:
        x = 1 / x
        n = -n

    result = 1

    while n:
        if n % 2 == 1:
            result *= x

        x *= x
        n //= 2

    return result


if __name__ == "__main__":
    x = 2.0
    n = 10

    print(my_pow(x, n))