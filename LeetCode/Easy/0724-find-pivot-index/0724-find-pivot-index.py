from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        result = -1
        l, r = 0, sum(nums)
        for i in range(len(nums)):
            r -= nums[i]
            if l == r:
                result = i
                break
            else:
                l += nums[i]

        return result
        