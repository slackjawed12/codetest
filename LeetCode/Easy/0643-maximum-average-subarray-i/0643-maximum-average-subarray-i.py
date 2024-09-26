from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur = sum(nums[:k])
        mx = cur
        result = mx / k

        for i in range(k, len(nums)):
            cur = cur - nums[i-k] + nums[i]
            if cur >= mx:
                mx = cur
                result = mx / k

        return result
            
            