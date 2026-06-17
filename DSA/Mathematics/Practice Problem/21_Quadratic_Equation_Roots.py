"""
Problem: Quadratic Equation Roots
Difficulty: Basic

Question:
Given a quadratic equation:

ax² + bx + c = 0

Find its roots.

If roots are real:
- Return floor value of each root
- Return them in decreasing order

If roots are imaginary:
- Return ["Imaginary"]

Examples:

Input: a = 1, b = -2, c = 1
Output: [1, 1]

Input: a = 1, b = -7, c = 12
Output: [4, 3]

Constraints:
-10³ ≤ a, b, c ≤ 10³

Approach:
1. Compute the discriminant:

   D = b² - 4ac

2. If D < 0:
   Roots are imaginary.

3. Otherwise use the quadratic formula:

   x₁ = (-b + √D) / (2a)
   x₂ = (-b - √D) / (2a)

4. Take floor values and return in decreasing order.

Time Complexity: O(1)
Space Complexity: O(1)
"""

import math


def quadratic_roots(a, b, c):
    discriminant = b * b - 4 * a * c

    if discriminant < 0:
        return ["Imaginary"]

    sqrt_d = math.sqrt(discriminant)

    x1 = math.floor((-b + sqrt_d) / (2 * a))
    x2 = math.floor((-b - sqrt_d) / (2 * a))

    return [x1, x2] if x1 > x2 else [x2, x1]


if __name__ == "__main__":
    a = 1
    b = -7
    c = 12

    print(quadratic_roots(a, b, c))