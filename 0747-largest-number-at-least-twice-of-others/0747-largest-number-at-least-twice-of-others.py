class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        f, s = -1, -1
        for i,n in enumerate(nums):
            if n > nums[f] or f == -1:
                f = i
                
        for i,n in enumerate(nums):
            if i == f:
                continue

            s = i if n >= nums[s] or s == -1 else s
            
        return f if nums[f] >= nums[s] * 2 else -1