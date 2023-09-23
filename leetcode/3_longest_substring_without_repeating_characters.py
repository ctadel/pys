"""

3. Longest Substring Without Repeating Characters
Medium

Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
Accepted
4.9M
Submissions
14.5M
Acceptance Rate
34.0%
"""

# ROUGH
# def sub_str(string):
#     longest_substring = ''
#     current_substring  = ''

#     for letter in string:

#         if letter not in current_substring:
#             current_substring = current_substring + letter

#         else:
#             if len(longest_substring) < len(current_substring):
#                 longest_substring = current_substring

#             current_substring = current_substring[current_substring.find(letter)+1:] + letter

#     if len(longest_substring) < len(current_substring):
#         longest_substring = current_substring

#     return longest_substring

# output = sub_str('dvdf')
# print(len(output), output)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring_length = 0
        current_substring  = ''

        for letter in s:

            if letter not in current_substring:
                current_substring = current_substring + letter

            else:
                if longest_substring_length < len(current_substring):
                    longest_substring_length = len(current_substring)

                current_substring = current_substring[current_substring.find(letter)+1:] + letter

            if longest_substring_length < len(current_substring):
                longest_substring_length = len(current_substring)

        return longest_substring_length
