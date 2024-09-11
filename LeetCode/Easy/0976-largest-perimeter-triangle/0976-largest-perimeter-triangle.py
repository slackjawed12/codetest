class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()
        result = 0
        for r in range(2, len(nums)):
            if nums[r-2] + nums[r-1] > nums[r]:
                result = nums[r-2] + nums[r-1] + nums[r]
            
        return result