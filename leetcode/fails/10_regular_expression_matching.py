"""
10. Regular Expression Matching
Hard

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).



Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".


Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
Accepted
857.6K
Submissions
3.1M
Acceptance Rate
27.9%
"""



class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        p_pointer = 0
        super_char = False

        for index, char in enumerate(s):

            if p_pointer > len(p) - 1:
                return False

            # cases like a*a where current pointer is still in '*' and next was left to traverse
            # if index == len(s) - 1:

            #     # if p[p_pointer] == '*' and p_pointer < len(p) - 1 and p[p_pointer + 1] == char:
            #     if super_char:
            #         p_pointer += 1
            #         continue

            if super_char:
                if index == len(s) - 1 and char == p[p_pointer]:
                    p_pointer += 1
                    continue

                if char == p[p_pointer]: continue
                elif p_pointer >= len(p) - 1: return False
                else:
                    super_char = False
                    p_pointer += 1


            if (p[p_pointer] == char) or (p[p_pointer] == '.'):
                p_pointer += 1
                continue


            # current char must be equal to last character
            if p_pointer != 0 and p[p_pointer] == '*':


                # check for super character case eg: a*a
                if (p_pointer < len(p) - 1) and p[p_pointer + 1] == p[p_pointer - 1]:
                    super_char = True
                    p_pointer += 1
                    continue

                # move the pointer forward if last character is repeating
                if p[p_pointer - 1] == char or p[p_pointer - 1] == '.':
                    continue

                # # move the pointer forward if next character is also same
                # if s[index + 1] == char:
                #     p_pointer += 1
                #     continue

                # move the pointer forward if we have current character next in pattern
                if (p_pointer < len(p) - 1) and p[p_pointer + 1] in {char, '.'}:
                    p_pointer += 2
                    continue

                return False


            # last character is a ghost character and doesnot exist at all
            if (p_pointer < len(p) - 1) and p[p_pointer + 1] == '*':
                if p_pointer + 2 < len(p) and p[p_pointer + 2] == char:
                    if index == len(s) - 1: p_pointer += 3
                    else: p_pointer += 2

                else: return False


        pattern = p[p_pointer:]
        if pattern:
            if pattern == '*': return True
            return False


        return True


string  = 'aa'
pattern = 'a*a'

solution = Solution().isMatch(string, pattern)
print(solution)
