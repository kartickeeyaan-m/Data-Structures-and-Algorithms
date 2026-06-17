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
Use Binary Exponentiation (Exponentiation by Squaring).

If n is odd:
    multiply current x into result

Square x each iteration and divide n by 2.

This reduces the exponent exponentially.

Time Complexity: O(log n)
Space Complexity: O(1)
"""


def my_pow(x, n):
    if n == 0:
        return 1

    if n < 0:
        x = 1 / x
        n = -n

    result = 1

    while n > 0:
        if n % 2 != 0:
            result *= x

        x *= x
        n //= 2

    return result


if __name__ == "__main__":
    x = 2.0
    n = 10

    print(my_pow(x, n))