'''
Absolute Value


You are given an interger n, find the absolute value of the integer n.

Examples:

Input: n = -32
Output: 32
Explanation:The absolute value of -32 is 32.

Input: n = 45
Output: 45
Explanation: The absolute value of 45 is 45 itself.

Constraints:
-106 ≤ n ≤ 106

'''
class Solution:
    def absolute(self, n):
        if n >= 0:
            return n
        return -n


def main():
    n = int(input("Enter an integer: "))

    obj = Solution()
    result = obj.absolute(n)

    print("Absolute Value:", result)


if __name__ == "__main__":
    main()