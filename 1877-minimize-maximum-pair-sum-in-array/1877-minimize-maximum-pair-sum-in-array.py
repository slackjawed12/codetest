class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        for i in range(len(nums)//2):
            result = max(result, nums[i]+nums[len(nums)-i-1])
        
        return result
        