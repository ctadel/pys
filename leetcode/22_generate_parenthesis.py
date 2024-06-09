"""
22. Generate Parentheses
Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8

"""

from typing import *


class Solution:
    def working_function(self, n: int) -> List[str]:
        def dfs(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return

            if left < n:
                dfs(left + 1, right, s + '(')

            if right < left:
                dfs(left, right + 1, s + ')')

        res = []
        dfs(0, 0, '')
        return res

    def generateParenthesis(self, n: int) -> List[str]:

        if n == 1:
            return ["()"]

        nminus1 = self.generateParenthesis(n-1)
        enclosed = [f"({element})" for element in nminus1]
        multiplied = [f"(){element}" for element in nminus1]


        return enclosed + multiplied


n = 6

response = Solution().generateParenthesis(n)
actual = Solution().working_function(n)

print(len(response))
print(len(actual))
print(set(actual) - set(response))
