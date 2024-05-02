class Solution:
    def two_pointer_sort(self, array, left, mid, right):
        i = left
        j = mid
        temp = []

        while i < mid and j < right:
            if array[i] <= array[j]:
                temp.append(array[i])
                i += 1
            else:
                temp.append(array[j])
                j += 1

        if i < mid:
            temp.extend(array[i:mid])
        else:
            temp.extend(array[j:right])

        array[left:right] = temp

    def merge_sort(self, array:list, left, right):
        if right - left < 2:
            return

        # the old way
        # mid = (left + right) // 2

        # the modern way
        mid = left + (right - left) // 2

        self.merge_sort(array, left, mid)
        self.merge_sort(array, mid, right)
        self.two_pointer_sort(array, left, mid, right)


nums = [12, 5, 13, 1, 0, -5, 2, 15, 3, 11, 4]
print(nums)
response = Solution().merge_sort(nums, 0, len(nums))
print(nums)
