class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def isUnique(arr):
            s = set(arr)
            return len(arr) == len(s)

        cnt = 0
        while not isUnique(nums):
            nums = nums[3:]
            cnt += 1
        
        return cnt