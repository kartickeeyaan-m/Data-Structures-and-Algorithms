"""
Problem: Nth Term of GP from First Two Terms
Difficulty: Easy

Question:
Given the first two terms a and b of a Geometric Progression (GP),
find the nth term of the series.

Examples:

Input: a = 2, b = 3, n = 1
Output: 2

Explanation:
The first term itself is the answer.

Input: a = 1, b = 2, n = 5
Output: 16

Explanation:
Common ratio = 2

T5 = 1 × 2^(5−1)
   = 16

Constraints:
-10 ≤ a, b ≤ 10
1 ≤ n ≤ 9

Approach:
1. Compute the common ratio:

   r = b / a

2. Use the GP formula:

   Tn = a × r^(n−1)

Time Complexity: O(log n)
Space Complexity: O(1)
"""


def term_of_gp(a, b, n):
    if n == 1:
        return a

    r = b / a

    return a * (r ** (n - 1))


if __name__ == "__main__":
    a = 1
    b = 2
    n = 5

    print(term_of_gp(a, b, n))