"""
Problem: Trailing Zeroes in Factorial
Difficulty: Medium

Question:
For an integer n, find the number of trailing zeroes in n!.

Examples:

Input: n = 5
Output: 1
Explanation:
5! = 120, so the number of trailing zeroes is 1.

Input: n = 4
Output: 0
Explanation:
4! = 24, so the number of trailing zeroes is 0.

Constraints:
1 ≤ n ≤ 10^9

Approach:
A trailing zero is produced by a factor of 10.

10 = 2 * 5

Since factorials contain more factors of 2 than 5,
count the number of factors of 5.

Answer = n//5 + n//25 + n//125 + ...

Time Complexity: O(log₅ n)
Space Complexity: O(1)
"""


def trailing_zeroes(n):
    i = 5
    res = 0

    while i <= n:
        res += n // i
        i *= 5

    return res


if __name__ == "__main__":
    n = 5
    print(trailing_zeroes(n))