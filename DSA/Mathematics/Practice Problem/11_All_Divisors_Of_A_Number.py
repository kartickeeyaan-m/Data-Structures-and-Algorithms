"""
Problem: All Divisors of a Number
Difficulty: Easy

Question:
Given an integer n, return all the divisors of n in ascending order.

Examples:

Input: n = 20
Output: 1 2 4 5 10 20

Explanation:
20 is completely divisible by
1, 2, 4, 5, 10 and 20.

Input: n = 21191
Output: 1 21191

Explanation:
21191 is a prime number, so it has only
two divisors: 1 and 21191.

Constraints:
1 ≤ n ≤ 10^9

Approach:
Divisors always occur in pairs.

If i divides n, then n//i is also a divisor.

Store:
- Small divisors in one list.
- Large divisors in another list.

Finally combine:
small + reversed(large)

This produces ascending order without sorting.

Time Complexity: O(√n)
Space Complexity: O(k)

where k is the number of divisors.
"""


def get_divisors(n):
    small = []
    large = []

    i = 1

    while i * i <= n:
        if n % i == 0:
            small.append(i)

            if i != n // i:
                large.append(n // i)

        i += 1

    return small + large[::-1]


if __name__ == "__main__":
    n = 20
    print(get_divisors(n))