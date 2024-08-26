class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        result = 0
        before = -1
        for i in range(1, len(nums)-1):
            cur = nums[i]
            if before == cur:
                continue

            l, r = i-1, i+1
            while l > 0 and nums[l] == cur:
                l -= 1
            while r < len(nums)-1 and nums[r] == cur:
                r += 1
            
            left, right = nums[l], nums[r]
            if left < cur and cur > right:
                result += 1
            elif left > cur and cur < right:
                result += 1

            before = cur
        
        return result