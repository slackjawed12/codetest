class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        for i in range(len(nums)-1):
            a, b = nums[i], nums[i+1]
            if a%2 == b%2:
                return False
        
        return True