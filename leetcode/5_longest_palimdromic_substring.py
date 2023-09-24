"""
5. Longest Palindromic Substring
Medium

Hint
Given a string s, return the longest
palindromic

substring
 in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
Accepted
2.6M
Submissions
8M
Acceptance Rate
32.8%
"""

class Solution:

    def is_palindrome(self, string:str) -> bool:
        return string == string[::-1]

    # 1st solution
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)):
            window_size = len(s) - i

            cursor = 0
            while (cursor + window_size) <= len(s):
                if self.is_palindrome(s[cursor:cursor+window_size]):
                    return s[cursor:cursor+window_size]

                cursor += 1

    # 2nd solution
    # only works for palindrome midpoint as single letter
    # example: madam
    # and not for: baddab
    def longestPalindrome(self, s: str) -> str:

        palindrome_map = {}
        for cursor in range(len(s)):
            frame = 0

            while cursor-frame >= 0 and cursor+frame < len(s):

                current_string = s[cursor-frame : cursor+frame+1]

                if self.is_palindrome(current_string):
                    palindrome_map[frame] = current_string
                    frame += 1

                else:
                    break

        return palindrome_map


    def longestPalindrome(self, s: str) -> str:

        def expand(left, right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        string = ''
        for i in range(len(s)):
            string = max(string, expand(i,i), expand(i,i+1), key=len)
        return string



string = 'banana'
solution = Solution().longestPalindrome(string)

print(solution)
