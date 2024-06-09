"""
20. Valid Parentheses
Easy

Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""


class Solution:
    CLOSE = tuple(')}]')
    OPEN = tuple('({[')
    pairs = dict(zip(CLOSE, OPEN))

    def isValid(self, s: str) -> bool:
        stack = list()
        for i in s:
            if i in self.OPEN:
                stack.append(i)
            else:
                if self.pairs[i] != stack.pop():
                    return False
        return not stack


response = Solution().isValid('(){}[()]')
print(response)
