"""
28. Find the Index of the First Occurrence in a String
Easy
Topics
Companies
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.



Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def check_string(one, two):
            for i, j in zip(one, two):
                if i != j:
                    return False
            return True

        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if i+len(needle) > len(haystack):
                    return -1
                if check_string(haystack[i:i+len(needle)+1], needle):
                    return i
        return -1



haystack = "mississippi"
needle = "issipi"

result = Solution().strStr(haystack, needle)
print(result)
