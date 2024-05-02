from typing import *

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        left = lambda i: 0 if i==0 else flowerbed[i-1]
        right = lambda i: 0 if i==len(flowerbed)-1 else flowerbed[i+1]

        for i in range(len(flowerbed)):
            if flowerbed[i] == left(i) == right(i) == 0:
                flowerbed[i] = 1
                n -= 1

            if n <= 0:
                return True
        return False


flowerbed = [1,0,0,0,1,0,0]
n = 2

result = Solution().canPlaceFlowers(flowerbed, n)
print(result)
