from typing import *

"""
6. Zigzag Conversion
Medium

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"


Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
Accepted
1.1M
Submissions
2.4M
Acceptance Rate
45.9%
"""

class Solution:

    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows >= len(s):
            return s

        matrix = [[] for _ in range(numRows)]
        row = 0
        step = 1

        for letter in s:
            matrix[row].append(letter)

            if row == numRows - 1:
                step = -1

            if row == 0:
                step = 1

            row += step


        for row in range(numRows):
            matrix[row] = ''.join(matrix[row])

        return ''.join(matrix)



solution = Solution().convert('prajwal', 3)
print(solution)
