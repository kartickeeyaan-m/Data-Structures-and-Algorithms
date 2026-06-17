'''
Palindrome Number

Difficulty: Easy


You are given an integer n. Your task is to determine whether it is a palindrome.
A number is considered a palindrome if it reads the same backward as forward, as the number examples "12121" or "555".

Examples:

Input: n = 555
Output: true
Explanation: The number 555 reads the same backward as forward, so it is a palindrome.

Input: n = 123
Output: false
Explanation: The number 123 reads differently backward (321), so it is not a palindrome.

Input: n = -121
Output: true
Explanation: if number is palindrome, mainly ignore sign.

Constraints:
-109 ≤ n ≤ 109
'''

class Solution:
    def isPalindrome(self, n):
        if n < 0:
            n = -n

        dummy = n
        rev = 0

        while dummy:
            rem = dummy % 10
            rev = rev * 10 + rem
            dummy //= 10

        return rev == n


def main():
    n = int(input("Enter a number: "))

    obj = Solution()

    if obj.isPalindrome(n):
        print("Palindrome")
    else:
        print("Not Palindrome")


if __name__ == "__main__":
    main()