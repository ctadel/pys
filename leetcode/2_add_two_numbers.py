from typing import *
from datatypes import ListNode

"""
2. Add Two Numbers

Medium

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

Accepted
3.9M
Submissions
9.5M
Acceptance Rate
41.2%

"""

# Rough
#
# def add(l1, l2):
#     """
#         Input: l1 = [2,4,3], l2 = [5,6,4]
#         Output: [7,0,8]
#         Explanation: 342 + 465 = 807.
#     """
#     output = []
#     carry = False

#     def get_index(nums, i):
#         try:
#             return nums[i]
#         except: return 0

#     for index in range(max(len(l1),len(l2))):
#         sum = get_index(l1,index) + get_index(l2,index) + carry
#         carry = True if sum>9 else False
#         output.append(sum%10)

#     return output


# l1 = [2,4,3,3,5]
# l2 = [5,6,4]
# print(add(l1, l2))



# Definition for singly-linked list.
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = False
        output = ListNode()
        cursor=  output

        while l1 or l2 or carry:

            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            sum = num1 + num2 + carry
            carry = sum > 9

            element = ListNode(sum%10)
            cursor.next = element

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cursor = cursor.next

        return output.next


l1 = ListNode.from_iterable([8,3,2])
l2 = ListNode.from_iterable([9,2,1])


print(l1)
print(l2)

output = Solution().addTwoNumbers(l1, l2)
print("\nOUTPUT = ", output)
