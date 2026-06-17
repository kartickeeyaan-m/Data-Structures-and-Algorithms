'''

Count Digits

Given a number n, return the count of digits in this number.

Example:

Input: n = 1567
Output: 4
Explanation: There are 4 digits in 1567, which are 1, 5, 6 and 7.

Input: n = 255
Output: 3
Explanation: There are 3 digits in 255, which are 2, 5 and 5.

'''

class Solution:
    def countDigits(self, n):
        if n == 0:
            return 1

        count = 0

        while n:
            count += 1
            n //= 10

        return count


def main():
    n = int(input("Enter a number: "))

    obj = Solution()
    print("Number of digits:", obj.countDigits(n))


if __name__ == "__main__":
    main()