from typing import *

"""
4. Median of Two Sorted Arrays
Hard

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).


Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
Accepted
2.2M
Submissions
5.7M
Acceptance Rate
38.0%

"""

class Solution:

    def merge_two_lists(self, nums1: List[int], nums2: List[int]) -> List[int]:
        merged_list = []
        l_pointer = 0
        m_pointer = 0

        if not nums1:
            return nums2

        elif not nums2:
            return nums1

        for _ in range(len(nums1)+len(nums2)):
            try:
                l_value = nums1[l_pointer]
            except IndexError:
                merged_list.extend(nums2[m_pointer:])
                break

            try:
                m_value = nums2[m_pointer]
            except IndexError:
                merged_list.extend(nums1[l_pointer:])
                break


            if l_value <= m_value:
                merged_list.append(l_value)
                l_pointer += 1
            else:
                merged_list.append(m_value)
                m_pointer += 1


        return merged_list


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        #merge the two lists into one
        merged_list = self.merge_two_lists(nums1, nums2)
        print(merged_list)

        size = len(merged_list)

        if size%2 == 0:
            median = (merged_list[size//2 - 1] + merged_list[size//2]) / 2
        else:
            median = merged_list[size//2]

        return median


nums1 = [1,1,1,1,1,1,1,1,1,1,4,4]
nums2 = [1,3,4,4,4,4,4,4,4,4,4]


solution = Solution().findMedianSortedArrays(nums1, nums2)
print(solution)
