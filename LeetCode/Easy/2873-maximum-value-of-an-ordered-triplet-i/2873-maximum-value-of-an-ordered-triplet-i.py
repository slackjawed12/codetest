# brute force solution
class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        result = 0
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    result = max(result, (nums[i]-nums[j])*nums[k])
        
        return result

# optimized solution
class Solution2:
    def maximumTripletValue(self, nums: list[int]) -> int:
        ans = 0
        maxDiff = 0  
        maxNum = 0   

        for num in nums:
            ans = max(ans, maxDiff * num)
            maxDiff = max(maxDiff, maxNum - num)
            maxNum = max(maxNum, num)   

        return ans