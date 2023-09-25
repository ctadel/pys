"""
7. Reverse Integer
Medium

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
Accepted
2.8M
Submissions
10.1M
Acceptance Rate
27.9%
"""

class Solution:

    MAX_LIMIT = (2 ** 31) - 1
    MIN_LIMIT = -(2 ** 31)

    def reverse(self, x: int) -> int:
        value = str(x)[::-1]
        if value[-1] == '-':
            value = '-' + value[:-1]

        if int(value) in range(self.MIN_LIMIT, self.MAX_LIMIT):
            return int(value)
        else:
            return 0


num = -12356
solution = Solution().reverse(num)

print(num, " -> ", solution)
