class Solution:
    def threeSum(self, nums):
        triplets = []

        if len(nums) < 3: return []

        nums.sort()
        hashes = {num:index for index, num in enumerate(nums)}

        for i in range(len(nums) - 2):
            if nums[i] > 0 : break

            for j in range(i+1, len(nums) - 1):
                k_num = -1*(nums[i] + nums[j])
                k = hashes.get(k_num)

                if k and k > j:
                    _sort = [nums[i], nums[j], nums[k]].sort()
                    triplets.append(_sort)

        return triplets


nums = [3,0,-2,-1,1,2]
s = Solution().threeSum(nums)
print(s)
