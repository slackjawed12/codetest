class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = True
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                inc = False
                break
        
        dec = True
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                dec = False
                break
        
        return inc or dec
                