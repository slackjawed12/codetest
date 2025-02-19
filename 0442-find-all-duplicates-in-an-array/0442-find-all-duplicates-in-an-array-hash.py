class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s = set(nums)
        result = []
        for num in nums:
            if num in s:
                s.remove(num)
            else:
                result.append(num)
        
        return result